# Check whether a device responds to one ping 
import subprocess
ip_addresses = ["127.0.0.1", "127.0.0.1"]

for ip_address in ip_addresses: 
    result = subprocess.run(["ping", "-c", "1", ip_address])
    if result.returncode == 0:
        print("Device is reachable")
    else:
        print("No ping reply")

