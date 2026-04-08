from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ActionRequest(BaseModel):
    action: str

@app.post("/reset")
def reset():
    return {
        "observation": "plastic",
        "info": {}
    }

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
