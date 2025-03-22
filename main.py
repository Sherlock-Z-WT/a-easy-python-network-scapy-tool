from ping3 import ping#用于发送ICMP ping请求
import time#计算扫描耗时
from concurrent.futures import ThreadPoolExecutor #多线程核心库
def scan_ip(subnet ="172.22.53",start = 1,end = 255, threads=100):
    """
    多线程扫描局域网设备
    :param subnet: 子网地址
    :param start: 起始IP的末位
    :param end: 结束IP的末位
    :param threads: 并发线程数
    :return: 可达IP列表，总扫描的IP总数
    """
    #生成所有要扫描的地址列表
    ips = [f"{subnet}.{i}" for i in range(start, end + 1)]
    total_ips =len(ips)#计算出总的IP数量
    reachable_ips = []#存储可达IP的列表
    def check_ip(ip):
        """
        检查单个IP的可达性（线程任务函数）
        :return: 可达就return IP，不可达就return None
        """
        try:
            #发送ping请求（设置超时两秒，返回单位为毫秒ms）
            responses_time = ping(ip,timeout=2,unit="ms")
            if responses_time is not None:
                #绿色显示可达IP
                print(f"\033[32m{ip}可达，延迟为：{responses_time:.2f}秒\033[0m")
                return ip
            else:
                #红色显示不可达IP
                print(f"\033[31m{ip}不可达\033[0m")
                return None
        except PermissionError:
            print(f"\033[31m{ip}错误，需要管理员程序运行操作\033[0m")
            return None
        except Exception as e:
            #黄色显示其他异常信息
            print(f"\033[33m{ip}错误，原因是{e}\033[0m")
            return None
    #创建线程池执行扫描任务
    with ThreadPoolExecutor(max_workers=threads) as executor:
        #提交所有IP检测任务，map会自动分配任务给线性池
        results = executor.map(check_ip, ips)
        #遍历结果收集可达IP
        for result in results:
            if result:#过滤掉不可达IP，即None
                reachable_ips.append(result)
    return reachable_ips,total_ips
if __name__ =="__main__":
    #记录扫描开始时间
    start_time = time.time()
    #执行扫描获取结果
    reachable_ips, total_ips = scan_ip()
    #计算在线设备数量
    online_ips = len(reachable_ips)
    #输出扫描耗时,保留三位小数
    print(f"扫描完成，总共耗时:{(time.time()-start_time)*1000:.3f}ms")#转换为毫秒
    #格式化输出可达设备列表
    print("\n可达设备列表：")
    if len(reachable_ips) > 0:
        #每行显示5个IP的分页逻辑
        for i in range(0, len(reachable_ips), 10):  # 步长10表示每行10个
            line = reachable_ips[i:i + 10]  # 切片获取当前行IP
            print("  " + ", ".join(line))  # 用逗号分隔
    else:
        print("  (未发现任何在线设备)")
    #输出统计信息
    print(f"总共发现设备{total_ips}台，实际在线设备数量{online_ips}台")
