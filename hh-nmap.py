#!/bin/python3
import argparse
import nmap
import re

def run_nmap(ip, quick=True, ports=False):
    nm = nmap.PortScanner()
    if ports == False:
        if quick:
            ports = "21-500,631,993-1080,1443,8080,8443"
        else:
            ports = "1-65535"
    scan = nm.scan(ip, ports, arguments="-Pn")
    return scan["scan"][ip]['tcp']

def parse_targets(file):
    with open(file, 'r') as f:
        content = f.read()
        regex = r'(?m)Target: (.*)\n(:?.+(?:\r\n|[\r\n]))*'
        regex = re.compile(r'Target: (.*?)[^\S\r\n]*[\[\+\]]', re.DOTALL)
        targets = re.findall(regex, content)
        out = []
        for target in targets:
            target = target.replace("\r\n", "\n").strip().split("\n")
            out.append(target)
        return out
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog='hh-nmap.py',
                        description='Read a txt file from hosthunter and run nmap on them.',
                        epilog='Author: Daniel Weisinger')


    parser.add_argument('targets')
    parser.add_argument('-F', '--quick', action="store_true", default=True)
    parser.add_argument('-p', '--all', action="store_true", default=False)
    parser.add_argument('-P', '--ports', default=False)

    args = parser.parse_args()

    if args.all and args.quick:
        print("Multiple scan options set, defaulting to --all")
        args.quick = False
    
    if args.ports != False:
        print("Scanning custom ports: " + args.ports)

    targets = parse_targets(args.targets)
    for target in targets:
        print("--------------")        
        print("Checking " + target[0])
        for i in range(1, len(target)):
            print(target[i])
        nmr = run_nmap(target[0], quick=args.quick, ports=args.ports)
        print(' ')
        print('Protocol : tcp')
        lport = nmr.keys()
        sorted(lport)
        for port in lport:
            if nmr[port]['state'] != "closed":
                print ('port : %s\tstate : %s' % (port, nmr[port]['state']))