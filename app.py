from fastapi import FastAPI
from env import SupportEnv

app = FastAPI()

env = SupportEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()
