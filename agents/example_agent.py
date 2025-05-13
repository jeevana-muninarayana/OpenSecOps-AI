class ExampleAgent:
    def run(self, input_data, context):
        # Simple data inspection logic for demo
        findings = []
        for key, value in input_data.items():
            if isinstance(value, str) and "error" in value.lower():
                findings.append(f"Potential issue in {key}: '{value}'")
        return {"findings": findings, "context_used": context}
