# Check whether a device responds to one ping 
import subprocess
ip_addresses = ["127.0.0.1", "127.0.0.1"]

reachable_count = 0
for ip_address in ip_addresses:
    result = subprocess.run(["ping", "-c", "1", ip_address], capture_output=True)
    if result.returncode == 0:
        print(ip_address, "is reachable")
        reachable_count += 1
    else:
        print(ip_address, "gave no ping reply")

print(reachable_count, "addresses replied")

