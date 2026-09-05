"""Bounded ML advisor. It recommends actions; it never establishes payment truth."""

def recommend(features: dict) -> dict:
    return {"recommended_action": "WAIT_AND_VERIFY", "confidence": 0.0}
