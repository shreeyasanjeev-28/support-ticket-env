from fastapi import FastAPI
from env import SupportEnv, Action

app = FastAPI()
env = SupportEnv()

@app.post("/reset")
def reset():
    try:
        obs = env.reset()
        return obs.dict()
    except Exception as e:
        return {"error": str(e)}

@app.post("/step")
def step(action: Action):
    try:
        obs, reward, done, info = env.step(action)
        return {
            "observation": obs.dict(),
            "reward": float(reward),
            "done": done,
            "info": info
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/state")
def state():
    try:
        return env.state()
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def root():
    return {"status": "running"}
