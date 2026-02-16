# Python TCP Port Scanner

A simple TCP port scanner built using Python.

## Features

- Scan target by IP or domain
- Custom port range
- Adjustable timeout
- Multi-threaded scanning

## Technologies Used

- socket
- argparse
- concurrent.futures (ThreadPoolExecutor)
- datetime

## Usage

Basic scan:

''bash
python portscan.py example.com
python portscan.py 192.168.1.10 --start 1 --end 1024
python portscan.py 127.0.0.1 --start 79 --end 82 --workers 10 --timeout 0.5

## Command-Line Options

- target : Hostname or IP address
- --start : Starting port (default: 1)
- --end : Ending port (default: 65535)
- --workers : Maximum worker threads (default: 100)
- --timeout : Socket timeout in seconds (default: 1.0)

## Legal Notice

Only scan systems you own or have permission to test.
Unauthorized scanning may violate laws or network policies.

