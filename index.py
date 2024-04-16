import argparse
import socket
import requests


# function for argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description='Accept and display domain\
                                     name')
    parser.add_argument('--domain', '-d', required=True, help='Domain name')
    args = parser.parse_args()
    return args


# function to resolve domain to IP address
def domain_resolver(domain):
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        return None
    else:
        return ip_address


# function to query shodan for cpe and hostname data
def query_shodan(ip_address):
    try:
        response = requests.get(f'https://internetdb.shodan.io/{ip_address}')
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    else:
        return response.json()


def main():
    args = parse_arguments()
    print(f'Domain: {args.domain}')
    ip_address = domain_resolver(args.domain)
    if ip_address:
        print(f'IP address: {ip_address}')
        data = query_shodan(ip_address)
        if data:
            print(f'There are {len(data["cpes"])} CPEs for domain\
 {args.domain}')
            for cpes in data['cpes']:
                print(f'  {cpes}')
            print(f'There are {len(data["hostnames"])} Hostnames for domain\
 {args.domain}')
            for hostname in data['hostnames']:
                print(f'  {hostname}')
        else:
            print('Error: Unable to obtain data')
    else:
        print('Error: Unable to resolve domain')


if __name__ == '__main__':
    main()
