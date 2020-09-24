#!/usr/bin/env python3
"""drone-ssl-hosts

Usage:
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

"""
import os
from sys import exit
from ipaddress import ip_network,ip_address
import urllib3
from docopt import docopt
from pylair import models,client
from pprint import pprint
import ssl, socket

def get_connection_details(args):
    conx = {}
    try:
        lair_url = os.environ['LAIR_API_SERVER']
        u = urllib3.util.parse_url(lair_url)
        conx['username'],conx['password'] = u.auth.split(":")
        conx['username'] = str(conx['username']).replace('%40','@')
        conx['scheme'] = u.scheme
        conx['port'] = u.port
        if u.scheme == 'https' and u.port == None:
            conx['port'] = 443 
    except KeyError:
        pass

    if args['-u']:
        conx['username'] = args['-u']
    if args['-p']:
        conx['password'] = args['-p']
    if args['-U']:
        url = urllib3.util.parse_url(args['-U'])
        conx['hostname'] = url.hostname
        if url.scheme == 'https' and url.port == None:
            conx['port'] = 443
        conx['scheme'] = url.scheme
    return conx

def get_hostnames(ip, port):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    s = ctx.wrap_socket(socket.socket()) 
    s.connect((ip, port))
    cert = s.getpeercert()
    subject = dict(x[0] for x in cert['subject'])
    issued_to = subject['commonName']
    alt_names = list(x[1] for x in cert['subjectAltName'])
    
    hostnames = []
    if "*" not in issued_to:
        hostnames.append(issued_to)

    for name in alt_names:
        if name not in hostnames:
            hostnames.append(name)

    return hostnames


def main():
    arguments = docopt(__doc__, version='drone-whois 2.0.0')
    conx_details = get_connection_details(arguments)

    project_id = arguments['<id>']
    project = dict(models.project)
    project['id'] = project_id
    project['commands'] = [{'command': 'ssl', 'tool': 'sockets'}]
    project['tool'] = 'drone-ssl-hosts'

    opts = client.Options(conx_details['username'],
                          conx_details['password'],
                          conx_details['hostname'] + ":" + str(conx_details['port']),
                          project_id,
                          scheme=conx_details['scheme'],
                          insecure_skip_verify=arguments['-k'])

    try:
        lines = [line.rstrip('\n') for line in open(arguments['<file>'])]
    except IOError as e:
        print("Fatal: Could not open file. Error: ",e)
        exit(1)

    for line in lines:
        host = tuple(line.split(':'))
        ip = host[0]
        port = int(host[1])
        hostnames = get_hostnames(ip,port)

        for name in hostnames:
            resolves_to = socket.gethostbyname(name)
            if str(resolves_to) != ip:
               hostnames.delete(name)

        host = dict(models.host)
        host['ipv4'] = ip
        host['Hostnames'] = hostnames
        host['LastModifiedBy'] = 'drone-ssl-hosts'
        host['projectId'] = project_id
        project['hosts'].append(host)

    res = client.import_project(project, opts)
    if res['status'] == 'Error':
        print("Fatal: ",res['message'])
        print(project)
        exit(1)
    print("Success: Operation completed successfully")
      

if __name__ == '__main__':
    main()
