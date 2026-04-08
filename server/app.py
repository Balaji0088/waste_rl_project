from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

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

# ✅ REQUIRED main function
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

# ✅ REQUIRED entry point
if __name__ == "__main__":
    main()
