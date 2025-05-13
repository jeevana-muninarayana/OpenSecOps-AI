from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from agents.registry import AGENT_REGISTRY

app = FastAPI(title="OpenSecOps AI", description="Modular Agentic Security Platform", version="0.1")

class InvestigationRequest(BaseModel):
    agent_name: str
    input_data: dict
    context: Optional[dict] = {}

@app.post("/investigate")
def investigate(request: InvestigationRequest):
    agent = AGENT_REGISTRY.get(request.agent_name)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    try:
        result = agent.run(request.input_data, request.context)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
