from consolemenu import *
from consolemenu.items import *
import nmap
import json
import toolkit

nmap = nmap.PortScanner()

def main():
    show_menu = ConsoleMenu("NMAP TOOLKIT", "This automates NMAP for you ;)", show_exit_option=True, exit_option_text='[+] '
                                                                                                                 'Quit',
                       clear_screen=True)
    target = input('Target: ')
    scan_type = input('Would you like to scan a single computer, or the whole network? (single, network) ')
    if scan_type.lower() == 'single':
        target=target
    elif scan_type.lower() == 'network':
        target += '/24'
    else:
        return "Select an option!"
    nmap_os = FunctionItem('[+] OS Detection', nmapos(target))
    nmap_dns = FunctionItem('[+] DNS Scan', nmapdns(target))
    nmap_version = FunctionItem('[+] Version Detection', nmapversion(target))
    nmap_ports = FunctionItem('[+] Port Scan', nmapports(target))
    nmap_all = FunctionItem('[+] Full Scan', nmapall(target))
    back_option = FunctionItem('[+] Back', toolkit.main)
    # main_menu = FunctionItem('[+] Main Menu', menu.main())
    show_menu.append_item(nmap_os)
    show_menu.append_item(nmap_dns)
    show_menu.append_item(nmap_version)
    show_menu.append_item(nmap_ports)
    show_menu.append_item(nmap_all)
    show_menu.append_item(back_option)
    # show_menu.append_item(main_menu)
    show_menu.show(show_exit_option=True)

def nmapos(target):
    print(f"\nScanning {target} for OS Detection, please wait...")
    os_results = nmap.scan(target,None,'-A')
    print(json.dumps(os_results, indent=4, sort_keys=True))
    return os_results


def nmapdns(target):
    print(f"\nScanning {target} for DNS detection, please wait...")
    dns_results = nmap.scan(target,'53', '')
    print(json.dumps(dns_results, indent=4, sort_keys=True))
    return dns_results

def nmapversion(target):
    print('Welcome to the NMAP Version Scan ')
    print(f"\nScanning {target} for Version Detection, please wait...")
    version_results = nmap.scan(target, None,'--top-ports 1000 -sV')
    print(json.dumps(version_results, indent=4, sort_keys=True))
    return version_results

def nmapports(target):
    print('Welcome to the NMAP Port Scan Module')
    print(f"\nScanning {target} for Port Scan, please wait...")
    ports = nmap.scan(target, None, '--top-ports 1000 -sV')
    print(json.dumps(ports, indent=4, sort_keys=True))
    return ports

def vulns(target):
    print('Welcome to the vuln scan module!')
    print(f'Scanning {target} for vulnerabilities, please wait...')
    vulners = nmap.scan(target, None, '--script=vulners.nse')
    print(json.dumps(vulns, indent=4, sort_keys=True))
    return vulners

def nmapall(target):
    print('Welcome to the NMAP Full Scan Module')
    print("\nScanning, please wait: " + target)
    print("\nDetecting os...")
    os_results = nmapos(target)
    print("\nSuccess!! Scanning dns...")
    dns_results = nmapdns(target)
    print("\nSuccess!! Detecting version...")
    version_results = nmapversion(target)
    print("\nSuccess!! Scanning top ports...")
    ports = nmapports(target)
    print("\nSuccess!! Scanning for known vulnerabilities...")
    vulners = vulns(target)
    print("\nSuccess! All scans finished, compiling results...")
    print(json.dumps(os_results, indent=4, sort_keys=True))
    print(json.dumps(dns_results, indent=4, sort_keys=True))
    print(json.dumps(version_results, indent=4, sort_keys=True))
    print(json.dumps(ports, indent=4, sort_keys=True))
    print(json.dumps(vulners, indent=4, sort_keys=True))
    return os_results, dns_results, version_results, ports, vulners

if __name__ == '__main__':
    main()