from fastapi import FastAPI
from env import SupportEnv, Action

app = FastAPI()

@app.get("/")
def run_env():
    env = SupportEnv()
    obs = env.reset()

    # simple logic
    if "order" in obs.ticket.lower():
        reply = "Sorry, I will track your order."
    elif "damaged" in obs.ticket.lower():
        reply = "We will provide refund or replacement."
    else:
        reply = "We will escalate this issue."

    action = Action(response=reply)
    _, reward, _, info = env.step(action)

    return {
        "ticket": obs.ticket,
        "response": reply,
        "reward": reward,
        "task_level": info["task_level"]
    }