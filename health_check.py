# Check whether a device responds to one ping 
import subprocess

ip_address = input("Enter an IP address: ")

result = subprocess.run(["ping", "-c", "1", ip_address])

if result.returncode == 0:
    print("Device is reachable")
else:
    print("No ping reply")

