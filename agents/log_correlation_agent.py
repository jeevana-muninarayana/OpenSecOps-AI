class LogCorrelationAgent:
    def run(self, input_data, context):
        # Expecting input_data = { "cloudtrail": [...], "edr": [...], "iam": [...] }
        indicators = {}
        sources = ["cloudtrail", "edr", "iam"]
        matches = []

        # Step 1: Extract indicators from each source
        for src in sources:
            for log in input_data.get(src, []):
                indicator = log.get("indicator")
                if not indicator:
                    continue
                if indicator not in indicators:
                    indicators[indicator] = set()
                indicators[indicator].add(src)

        # Step 2: Flag if indicator appears in 2 or more sources
        for indicator, seen_in in indicators.items():
            if len(seen_in) >= 2:
                matches.append({
                    "indicator": indicator,
                    "seen_in": list(seen_in),
                    "confidence": "High" if len(seen_in) == 3 else "Medium"
                })

        return {
            "correlated_alerts": matches,
            "total_indicators_checked": len(indicators),
            "context_used": context
        }
