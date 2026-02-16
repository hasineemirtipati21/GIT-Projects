# Import required modules
import argparse                      # For handling command-line arguments
import socket                        # For network connections
from datetime import datetime        # For measuring scan time
from concurrent.futures import ThreadPoolExecutor, as_completed  # For multithreading


def scan_port(target_ip: str, port: int, timeout: float) -> tuple[int, bool]:
    """
    Attempt to connect to a specific port on the target IP.

    Returns:
        (port, True)  -> if port is open
        (port, False) -> if port is closed or unreachable
    """
    try:
        # Create a TCP socket (IPv4 + TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)  # Set connection timeout
            result = s.connect_ex((target_ip, port))
            # connect_ex returns 0 if connection is successful
            return (port, result == 0)

    except Exception:
        # If any unexpected error occurs, treat port as closed
        return (port, False)


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments provided by the user.
    """
    p = argparse.ArgumentParser(description="Simple TCP port scanner")

    # Target hostname or IP address
    p.add_argument("target", help="Target hostname or IP address")

    # Starting port (default = 1)
    p.add_argument("--start", type=int, default=1,
                   help="Start port (default: 1)")

    # Ending port (default = 65535)
    p.add_argument("--end", type=int, default=65535,
                   help="End port (default: 65535)")

    # Socket timeout duration
    p.add_argument("--timeout", type=float, default=1.0,
                   help="Socket timeout seconds (default: 1.0)")

    # Number of concurrent threads
    p.add_argument("--workers", type=int, default=100,
                   help="Max concurrent workers (default: 100)")

    return p.parse_args()


def main() -> None:
    """
    Main function that coordinates the port scanning process.
    """

    # Parse user arguments
    args = parse_args()

    # Resolve hostname to IP address
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {args.target}")
        return

    # Record start time
    start_time = datetime.now()

    # Print scan information
    print("-" * 50)
    print(f"Scanning target: {args.target} ({target_ip})")
    print(f"Ports: {args.start} to {args.end}")
    print(f"Workers: {args.workers}, Timeout: {args.timeout}s")
    print(f"Time started: {start_time}")
    print("-" * 50)

    open_ports = []  # List to store open ports

    try:
        # Create thread pool for concurrent scanning
        with ThreadPoolExecutor(max_workers=args.workers) as executor:

            # Submit scan tasks for each port in range
            futures = {
                executor.submit(scan_port, target_ip, port, args.timeout): port
                for port in range(args.start, args.end + 1)
            }

            # Process results as they complete
            for fut in as_completed(futures):
                port, is_open = fut.result()
                if is_open:
                    print(f"Port {port} is open")
                    open_ports.append(port)

    except KeyboardInterrupt:
        # Handle manual interruption (Ctrl+C)
        print("\nScan interrupted by user")
        return

    # Record end time
    end_time = datetime.now()

    # Print summary
    print("-" * 50)
    print(f"Scan completed in: {end_time - start_time}")

    if open_ports:
        print("Open ports found:")
        for p in sorted(open_ports):
            print(f" - {p}")
    else:
        print("No open ports found")


# Entry point of the program
if __name__ == "__main__":
    main()
