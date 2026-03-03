from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/add")
async def add(a: Optional[float] = 0, b: Optional[float] = 0):
    try:
        s = float(a) + float(b)
    except Exception:
        return {"error": "invalid inputs"}
    return {"a": a, "b": b, "sum": s}
