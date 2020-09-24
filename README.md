# drone-ssl-hosts
Drone for importing hostnames based on SSL/TLS certificate information into Lair.  
  
The purpose of this drone is to determine hostnames for a give set of IP addresses and ports. It does this by establishing a connection to each IP address at the given port and retrieving the SSL/TLS certificate presented by the server. The drone then retrieves the subject name and the subject alternate names of the certificate and performs DNS lookups on each of the hostnames associated with the certificate. For each hostname that resolves back to the original IP address, it adds that hostname to the host in Lair with that IP address.
  
# Install
This library is dependent on pylair. After installing pylair, download the latest release [here](https://github.com/x-a-n-d-e-r-k/drone-ssl-hosts/releases/latest).  
  
$ sudo pip3 install drone-ssl-hosts*.tar.gz
or 
$ sudo pip3 install https://github.com/x-a-n-d-e-r-k/drone-ssl-hosts/releases/download/v1.0.0/drone-ssl-hosts-1.0.0.tar.gz
or 
$ sudo python3 -m pip install https://github.com/x-a-n-d-e-r-k/drone-ssl-hosts/releases/download/v1.0.0/drone-ssl-hosts-1.0.0.tar.gz
  
# Usage  
      drone-ssl-hosts [-k] [-u=<username>] [-p=<password>] [-U=<url>] <id> <file>  
      drone-ssl-hosts --version  
      drone-ssl-hosts (-h | --help)  
  
# Options
      -h --help       Show usage.  
      --version       Show version.  
      -k              Allow insecure SSL connections.  
      -u=<username>   Lair Username  
      -p=<password>   Lair Password  
      -U=<url>        Lair API URL   
  
drone-ssl-hosts will also make use of the LAIR_API_SERVER environment variable if it is set. If you choose to use the environment variable, you can exclude the -u, -p, and -U options.

# File Example  
  127.0.0.1:443  
  127.0.0.2:8443  
  127.0.0.3:8080  



