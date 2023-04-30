# hosthunter-nmap
A port scan utility that takes the output of a HostHunter scan and runs a port scan on each target.

## Install Required Packages
```
pip3 install -r requirements.txt
```

## Run hh-nmap.py

### Quick Scan
```
python3 hh-nmap.py -F hosthunter-output.txt
```
OR
```
python3 hh-nmap.py --quick hosthunter-output.txt
```

### Full Scan
```
python3 hh-nmap.py -p hosthunter-output.txt
```
OR
```
python3 hh-nmap.py --all hosthunter-output.txt
```

### Custom Scan
```
python3 hh-nmap.py -P 80,443,21-25 hosthunter-output.txt
```
OR
```
python3 hh-nmap.py --ports 80,443,21-25 hosthunter-output.txt
```

## hh-nmap.py Help
```
usage: nmap-all [-h] [-F] [-p] [-P PORTS] targets

Read a txt file from hosthunter and run nmap on them.

positional arguments:
  targets

options:
  -h, --help            show this help message and exit
  -F, --quick
  -p, --all
  -P PORTS, --ports PORTS

Author: Daniel Weisinger

```
