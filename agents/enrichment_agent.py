import datetime

class EnrichmentAgent:
    def run(self, input_data, context):
        enriched_data = []
        threat_db = {
            "1.2.3.4": {"threat_level": "High", "type": "Botnet", "last_seen": "2024-11-15"},
            "malicious.com": {"threat_level": "Medium", "type": "Phishing", "last_seen": "2024-10-03"},
        }

        for key, value in input_data.items():
            if isinstance(value, str) and value in threat_db:
                threat_info = threat_db[value]
                enriched_data.append({
                    "indicator": value,
                    "enrichment": threat_info,
                    "timestamp": datetime.datetime.utcnow().isoformat()
                })
        
        return {"enriched_findings": enriched_data, "context_used": context}
