# Domain Reconnaissance Tool

A simple Python tool for domain analysis that resolves domain names to IP addresses and retrieves additional reconnaissance information from Shodan's InternetDB.

## Features

- Resolves domain names to IP addresses
- Queries Shodan InternetDB for CPE (Common Platform Enumeration) data
- Retrieves associated hostnames for the target IP
- Clean command-line interface with error handling

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository
2. Install required dependencies:
```bash
pip install requests
```

## Usage

```bash
python domain_recon.py --domain example.com
```

or using the short flag:

```bash
python domain_recon.py -d example.com
```

## Example Output

```
Domain: example.com
IP address: 93.184.216.34
There are 2 CPEs for domain example.com
  cpe:/a:apache:http_server
  cpe:/o:linux:linux_kernel
There are 3 Hostnames for domain example.com
  example.com
  www.example.com
  mail.example.com
```

## Notes

- This tool uses Shodan's free InternetDB API (no API key required)
- CPE data helps identify software and operating systems running on the target
- Use responsibly and only on domains you own or have permission to analyze

## Error Handling

The tool gracefully handles:
- Invalid domain names
- Network connectivity issues
- API failures

## Disclaimer
This tool is intended for educational and authorized security testing purposes only. 
Only use this tool on domains you own or have explicit permission to analyze.

