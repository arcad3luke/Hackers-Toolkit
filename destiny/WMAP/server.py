# destiny/WMAP/server.py
from flask import Flask, jsonify, request
from destiny.WMAP.nmap_scan import run_nmap_scan, format_nmap_results
from destiny.WMAP.metasploit_scan import run_metasploit_scan, format_metasploit_results, SERVICE_MODULE_MAP
from destiny.keys import *

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the WMAP Flask server!"})

@app.route('/api/nmap', methods=['GET'])
def get_nmap_scan():
    target = request.args.get('target', '127.0.0.1')
    nm = run_nmap_scan(target)
    formatted_results = format_nmap_results(nm)
    return jsonify({
        "nmap_results": formatted_results
    })

@app.route('/api/metasploit', methods=['GET'])
def get_metasploit_scan():
    target = request.args.get('target', '127.0.0.1')
    username = request.args.get('username', keys['msfuser'])
    password = request.args.get('password', keys['msfpass'])
    msf_results = run_metasploit_scan(target, username, password)
    formatted_results = format_metasploit_results(msf_results)
    return jsonify({
        "metasploit_results": formatted_results
    })

@app.route('/api/vulnerability_scan', methods=['GET'])
def get_vulnerability_scan():
    target = request.args.get('target', '127.0.0.1')
    username = request.args.get('username', 'msf')
    password = request.args.get('password', 'yourpassword')

    # Run Nmap scan
    nm = run_nmap_scan(target)
    nmap_results = format_nmap_results(nm)

    # Run Metasploit scan based on Nmap results
    metasploit_results = []
    for host_info in nmap_results:
        for service_info in host_info['services']:
            service = service_info['service']
            port = service_info['port']
            if service in SERVICE_MODULE_MAP:
                msf_result = run_metasploit_scan(target, username, password)
                metasploit_results.append(msf_result)

    formatted_msf_results = format_metasploit_results(metasploit_results)

    return jsonify({
        "nmap_results": nmap_results,
        "metasploit_results": formatted_msf_results
    })

def run_server():
    app.run(debug=True)

if __name__ == '__main__':
    run_server()
