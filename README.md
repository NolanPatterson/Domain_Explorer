# Domain_Explorer

A Python command-line tool that resolves domain names to IP addresses and retrieves security-related information from Shodan's InternetDB API.

## Features

- **Domain Resolution**: Converts domain names to their corresponding IP addresses using DNS lookup
- **Shodan Intelligence**: Queries Shodan's InternetDB API to gather security metadata
- **CPE Detection**: Identifies Common Platform Enumeration (CPE) entries for discovered services
- **Hostname Enumeration**: Retrieves associated hostnames for target IP addresses
- **Error Handling**: Gracefully manages invalid domains, network issues, and API failures

## Requirements

- Python 3.6 or higher
- Required packages:
  - `requests` (for HTTP requests)
  - Standard library: `argparse`, `socket`

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:
```bash
pip install requests
```

## Usage

The script is executed using `domain_explorer.py` with the required `--domain` (or `-d`) argument:

```bash
python domain_explorer.py --domain example.com
```

Or using the short flag:
```bash
python domain_explorer.py -d example.com
```

### Command-Line Arguments

| Argument | Short | Required | Description |
|----------|-------|----------|-------------|
| `--domain` | `-d` | Yes | Domain name to resolve and analyze |

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

## Error Handling

The tool provides clear error messages for common issues:

- **Invalid Domain**: "Error: Unable to resolve domain"
- **Network/API Issues**: "Error: Unable to obtain data"
- **DNS Lookup Failure**: Gracefully handles non-existent domains

## How It Works

1. **Argument Parsing**: Accepts a domain name via command-line arguments
2. **DNS Resolution**: Uses `socket.gethostbyname()` to resolve the domain to an IP address
3. **Shodan API Query**: Makes a GET request to `https://internetdb.shodan.io/{ip_address}`
4. **Data Presentation**: Displays CPE entries and associated hostnames if data is available

## Notes

- Shodan's InternetDB API does not require an API key for basic queries
- CPE (Common Platform Enumeration) data helps identify software versions and operating systems
- The tool is read-only and only retrieves publicly available information

## Security & Legal Disclaimer

This tool is intended for authorized security research, penetration testing, and educational purposes only. **Always obtain explicit permission** before analyzing domains you do not own. Unauthorized reconnaissance may violate terms of service and applicable laws.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software, provided you include the original copyright notice. See the [LICENSE](LICENSE) file for the full license text.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
