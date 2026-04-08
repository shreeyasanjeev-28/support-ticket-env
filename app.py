from fastapi import FastAPI
from pydantic import BaseModel
from env import SupportEnv

app = FastAPI()

env = SupportEnv()

class Action(BaseModel):
    response: str

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()

# optional root endpoint
@app.get("/")
def root():
    return {"message": "OpenEnv Support Ticket Environment running"}
