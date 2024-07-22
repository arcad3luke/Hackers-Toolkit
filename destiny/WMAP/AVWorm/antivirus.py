# destiny/WMAP/antivirus.py
import requests
import keys
import os

class VirusTotalScanner:
    def __init__(self):
        self.file = input('Enter the name of the file you wish to scan: ')
        self.file_path = os.walk('./')

    API_KEY = Keys.keys['vtapikey']

    def scan_file(file_path):
        url = 'https://www.virustotal.com/api/v3/files'
        headers = {
            'x-apikey': API_KEY
        }
        files = {'file': (file_path, open(file_path, 'rb'))}
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to reach VirusTotal API"}

    def get_scan_report(file_id):
        url = f'https://www.virustotal.com/api/v3/files/{file_id}'
        headers = {
            'x-apikey': API_KEY
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to retrieve scan report from VirusTotal API"}

if __name__ == '__main__':
    VirusTotalScanner()