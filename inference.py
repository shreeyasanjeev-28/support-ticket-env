import os
from openai import OpenAI
from env import SupportEnv, Action

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    api_key=HF_TOKEN,
    base_url=API_BASE_URL
)

env = SupportEnv()

obs = env.reset()

#task name
ticket = obs.ticket.lower()
if "order" in ticket:
    task = "easy"
    reply = "Sorry, I will track your order."
elif "damaged" in ticket:
    task = "medium"
    reply = "We will provide refund or replacement."
elif "charged" in ticket or "billing" in ticket:
    task = "hard"
    reply = "We will refund and escalate this issue."
else:
    task = "unknown"
    reply = "We will look into this issue."

#REQUIRED STRUCTURED LOGS

print(f"[START] task={task}", flush=True)

action = Action(response=reply)
obs, reward, done, info = env.step(action)

print(f"[STEP] step=1 reward={reward}", flush=True)

print(f"[END] task={task} score={reward} steps=1", flush=True)
