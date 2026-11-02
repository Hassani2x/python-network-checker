# Python Network Checker

My first Python networking project. It uses a list and a loop
to ping each IP address once and report whether it replies.

## What I learned
- Variables and user input
- Running a system command with subprocess
- Checking return codes with if and else
- Adding comments to explain code
- Using lists and for loops to repeat checks

## How to run
On macOS, open Terminal in the project folder and run:
python3 health_check.py

The program automatically checks every entry in ip_addresses.
The example list contains 127.0.0.1 twice to test the loop
using my own computer.

## Limitations
No ping reply does not always mean a device is offline.
Some devices block ping.
