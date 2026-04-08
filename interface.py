import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# request schema
class ActionRequest(BaseModel):
    action: str

# ✅ RESET
@app.post("/reset")
def reset():
    return {
        "observation": "plastic",
        "info": {}
    }

# ✅ STEP
@app.post("/step")
def step(req: ActionRequest):
    state = "plastic"
    action = req.action.lower()

    reward = 1 if action == state else -1

    return {
        "observation": state,
        "reward": reward,
        "done": True,
        "info": {}
    }
