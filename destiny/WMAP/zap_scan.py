# destiny/WMAP/zap_scan.py
import requests

ZAP_API_KEY = keys.keys['zap_key']  # Replace with your OWASP ZAP API key
ZAP_URL = 'http://localhost:8080'

def start_zap_scan(target_url):
    scan_url = f'{ZAP_URL}/JSON/ascan/action/scan/?url={target_url}&apikey={ZAP_API_KEY}'
    response = requests.get(scan_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to reach OWASP ZAP API"}

def get_zap_scan_results(scan_id):
    results_url = f'{ZAP_URL}/JSON/ascan/view/scanProgress/?scanId={scan_id}&apikey={ZAP_API_KEY}'
    response = requests.get(results_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to retrieve scan results from OWASP ZAP API"}
