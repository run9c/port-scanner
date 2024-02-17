import argparse
import asyncio
import socket
import os
from pyfiglet import Figlet

# Custom banner
def print_banner():
    custom_fig = Figlet(font='slant')
    banner = custom_fig.renderText('Port Scanner')
    print(banner)
    print("made by marun")
    print()


async def port_scan(host, port, output_file):
    """
    Scan a port on the given host.
    """
    try:
        # Use asyncio.wait_for() to handle timeout
        reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=5)
        print(f"Port {port}: Open")
        output_file.write(f"Port {port}: Open\n")
        writer.close()
    except (ConnectionRefusedError, asyncio.TimeoutError):
        pass


async def scan_ports(host, ports, output_file):
    """
    Scan a range of ports on the given host.
    """
    print(f"Scanning ports for {host}...")
    tasks = [port_scan(host, port, output_file) for port in ports]
    await asyncio.gather(*tasks)


def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Fast Port Scanner")
    parser.add_argument("host", help="Host to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-100", help="Port range to scan, default is 1-100.")
    args = parser.parse_args()

    host = args.host
    port_range = args.port_range

    try:
        start_port, end_port = map(int, port_range.split("-"))
    except ValueError:
        print("Invalid port range. Please provide the range in the format 'start-end'.")
        return

    ports = [p for p in range(start_port, end_port + 1)]

    output_filename = f"port_scan_results_{host}.txt"

    with open(output_filename, "w") as output_file:
        asyncio.run(scan_ports(host, ports, output_file))

    print(f"\nScan completed. Results saved to '{output_filename}'.")


if __name__ == "__main__":
    main()