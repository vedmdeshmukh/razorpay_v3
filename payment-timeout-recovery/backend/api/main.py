from fastapi import FastAPI
from backend.recovery.resolver import resolve_timeout

app = FastAPI(title="Payment Timeout Recovery API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recovery/resolve-timeout")
def resolve_timeout_endpoint(payload: dict):
    return resolve_timeout(
        authoritative_status=payload.get("authoritative_status"),
        webhook_verified=bool(payload.get("webhook_verified", False)),
    )
