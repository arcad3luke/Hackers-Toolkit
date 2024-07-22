# destiny/WMAP/nmap_scan.py
import nmap
import time


def run_nmap_scan(target=input('Enter target IP address:')):
    nm = nmap.PortScanner()
    nm.scan(target)
    return nm

def format_nmap_results(nm):
    results = []
    for host in nm.all_hosts():
        host_info = {
            'host': host,
            'hostname': nm[host].hostname(),
            'state': nm[host].state(),
            'protocols': []
        }
        for proto in nm[host].all_protocols():
            protocol_info = {
                'protocol': proto,
                'ports': []
            }
            ports = nm[host][proto].keys()
            for port in ports:
                port_info = {
                    'port': port,
                    'state': nm[host][proto][port]['state']
                }
                protocol_info['ports'].append(port_info)
            host_info['protocols'].append(protocol_info)
        results.append(host_info)
    return results

def main():
    begin = run_nmap_scan()
    time.sleep(1)
    format_nmap_results(begin)

if __name__ == '__main__':
    main()