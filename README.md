# drone-ssl-hosts
Drone for importing hostnames based on SSL/TLS certificate information into Lair.  

The purpose of this drone is to determine hostnames for a give set of IP addresses and ports. It does this by establishing a connection to each IP address at the given port and retrieving the SSL/TLS certificate presented by the server. The drone then retrieves the subject name and the subject alternate names of the certificate and performs DNS lookups on each of the hostnames associated with the certificate. For each hostname that resolves back to the original IP address, it adds that hostname to the host in Lair with that IP address.

# Install
This library is dependent on pylair. After installing pylair, download the latest release here.  

$ sudo pip install drone-ssl-hosts*.tar.gz  

# Usage
   drone-ssl-hosts [-k] [-u=<username>] [-p=<password>] [-U=<url>] [-v] <id> <file>
   drone-ssl-hosts --version
   drone-ssl-hosts (-h | --help)

Options:
   -h --help       Show usage.
   --version       Show version.
   -v              Verbose output
   -k              Allow insecure SSL connections.
   -u=<username>   Lair Username
   -p=<password>   Lair Password
   -U=<url>        Lair API URL 

drone-ssl-hosts will also make use of the LAIR_API_SERVER environment variable if it is set. If you choose to use the environment variable, you can exclude the -u, -p, and -U options.

