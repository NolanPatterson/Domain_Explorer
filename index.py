# TODO: Use Python to find out more about a domain name entered by the user.
# You’ll take a domain name, convert it into an IP address, and query an API
# to get information about the server that hosts that website.

# TODO: Using the argparse module, create a required command line argument:
# --domain (or -d)
# This will require the user to input a domain name, such as “purdue.edu”,
# when running your program.

# TODO: Write a function that accepts a domain name as an argument and uses
# the socket.gethostbyname() function to obtain the IP address of the domain.
# If the domain can be resolved, return the IP address. Otherwise, return None.

# TODO: Write a function that accepts an IP address as an argument and uses
# the requests module get() function to query the Shodan API about that IP. If
# the API request can be successfully completed, return the results of the
# query as JSON. Otherwise, return None.

# TODO: In your main() method, read the value of the domain passed in by the
# user. Then obtain the IP address for the domain. Finally, obtain the data
# about the domain from the Shodan API. Once you have the details of the
# domain, print the information about the CPEs and the hostnames to the screen.
# If your program encounters an error either in resolving the domain or
# obtaining information from the API, write a simple error message to the
# screen and end the program.

if __name__ == '__main__':
    main()
