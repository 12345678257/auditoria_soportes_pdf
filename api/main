from fastapi import FastAPI
from engine.scorer import decide

app = FastAPI(title="Auditoría PDF Clínica API")

@app.post("/audit")
def audit(payload: dict):
    hits = payload.get("hits", [])
    decision = decide(hits)
    return {"decision": decision}
