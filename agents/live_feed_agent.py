import os
import requests

class LiveFeedAgent:
    def __init__(self):
        self.vt_key = os.getenv("VT_API_KEY")
        self.abuseip_key = os.getenv("ABUSEIPDB_API_KEY")

    def query_virustotal(self, ip):
        headers = {"x-apikey": self.vt_key}
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"VirusTotal error {response.status_code}"}

    def query_abuseipdb(self, ip):
        headers = {
            "Key": self.abuseip_key,
            "Accept": "application/json"
        }
        url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"AbuseIPDB error {response.status_code}"}

    def run(self, input_data, context):
        ip = input_data.get("ip")
        if not ip:
            return {"error": "Missing 'ip' in input_data"}

        vt_result = self.query_virustotal(ip)
        abuseip_result = self.query_abuseipdb(ip)

        return {
            "ip": ip,
            "virustotal": vt_result,
            "abuseipdb": abuseip_result
        }
