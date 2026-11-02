# Check whether a device responds to one ping 
import subprocess
ip_addresses = ["127.0.0.1", "127.0.0.1"]

for ip_address in ip_addresses: 
    result = subprocess.run(["ping", "-c", "1", ip_address], capture_output=True)
    if result.returncode == 0:
        print(ip_address, "is reachable")
    else:
        print(ip_address, "gave no ping reply")

