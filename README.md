# Python Network Checker

My first Python networking project. It asks for an IP address,
sends one ping, and reports whether the device replies.

## What I learned
- Variables and user input
- Running a system command with subprocess
- Checking return codes with if and else
- Adding comments to explain code

## How to run
On macOS, open Terminal in the project folder and run:
python3 health_check.py

Enter 127.0.0.1 to test your own computer.

## Limitations
No ping reply does not always mean a device is offline.
Some devices block ping.
