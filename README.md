# 🚀 Port Scanner

A fast and efficient port scanner written in Python.

## Features
- 🎉 Scans ports on a specified host quickly.
- 🖥️ Supports scanning a range of ports.
- 📝 Saves scan results to a text file.
- 🌈 Custom banner for a unique touch.
- 🛠️ Simple and easy-to-use command-line interface.

## 👇 Images 

### Program

<img src="https://github.com/run9c/port-scanner/blob/main/assets/image-1.png">

### Result

<img src="https://github.com/run9c/port-scanner/blob/main/assets/image-2.png">

## Usage
1. Install the required dependencies:

```
pip install argparse pyfiglet
```
2. Run the port scanner:
```python port_scanner.py <host> --ports <port_range>```

Example: `python port_scanner.py localhost --ports 1-1000`

3. View the scan results saved in a text file named `port_scan_results_<host>.txt`.

## Requirements
- Python 3.x
- argparse
- pyfiglet
