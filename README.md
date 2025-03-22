First，I want you to know:I am a college student who is 19 years old,and I am learning Python just now.I use 1 week to learn Python,and this is my first Python project. If you are a Python learner,than we can be friends,and I am happy to make friends with some Python learner,and we can talk about this together.I am waiting to your email!My email is in my homepage.

LAN IP scanner
This project provides an efficient multi-threaded LAN IP scanning tool that can quickly detect online devices within a given subnet. Through this tool, you can easily obtain the IP addresses and related latency information of reachable devices in the local area network, facilitating network management and device troubleshooting.
Installation instructions
To run this program, the ping3 library needs to be installed, which is used to send ICMP ping requests. You can install using pip through the following command:
pip install ping3
Ensure that your system has installed the Python environment, and it is recommended to use Python 3.6 or higher versions.
Usage
Directly run:
You can directly run the main.exe file to start the scan, which will scan IP addresses from 172.22.53.1 to 172.22.53.255 by default, using 100 concurrent threads. In the command line, enter the directory where the project is located and execute the following command:
python main.py
Custom scanning parameters:
If you want to customize the scanning range and concurrent thread count, you can modify the parameters of the scan_ip function. In the main. py file, find the following code snippet:
reachable_ips, total_ips = scan_ip()
You can modify it to:
reachable_ips, total_ips = scan_ip(subnet="192.168.1", start=1, end=100, threads=50)
The above code indicates scanning IP addresses from 192.168.1.1 to 192.168.1.100 using 50 concurrent threads.
Project Example
Assuming you run the default configured scan, after the scan is complete, you will see output similar to the following:
Scanning completed, total time: 234.567ms
List of reachable devices:
172.22.53.1,  172.22.53.5,  172.22.53.10,  172.22.53.15,  172.22.53.20
172.22.53.25,  172.22.53.30,  172.22.53.35,  172.22.53.40,  172.22.53.45
A total of 255 devices were discovered, but the actual number of online devices was 10
This indicates that out of the 255 scanned IP addresses, 10 devices are online and displays the IP addresses of reachable devices.

Contribution Guide
If you wish to contribute code or report issues to this project, please follow these steps:
Report issue: In the GitHub repository of the project, click on the "Issues" tab and then click on the "New issue" button. Provide a detailed description of the phenomenon of the problem, the environment in which the problem occurred, and possible steps for reproducing it.

Contribution code:
Firstly, fork the repository of this project to your own GitHub account.
In your fork repository, create a new branch with the recommended naming convention of feature/description or fix/description, such as feature/add more subnets or fix/ping timeout issue.
Make code modifications and improvements on the new branch.
After completing the modifications, submit the code and create a Pull Request to the original project repository. In the Pull Request, clearly describe your modification content and purpose.
