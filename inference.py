import os
from openai import OpenAI
from env import SupportEnv, Action

# Required environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN")

# OpenAI client (required by checklist)
client = OpenAI(
    api_key=HF_TOKEN,
    base_url=API_BASE_URL
)

env = SupportEnv()

# START log
print("START")

obs = env.reset()
print(f"STEP: Ticket -> {obs.ticket}")

# Rule-based baseline (no API dependency)
if "order" in obs.ticket.lower():
    reply = "Sorry, I will track your order."
elif "damaged" in obs.ticket.lower():
    reply = "We will provide refund or replacement."
elif "charged" in obs.ticket.lower():
    reply = "We will refund and escalate this issue."
else:
    reply = "We will look into this issue."

print(f"STEP: Response -> {reply}")

action = Action(response=reply)

obs, reward, done, info = env.step(action)

print(f"STEP: Reward -> {reward}")
print(f"STEP: Task Level -> {info['task_level']}")

# END log
print("END")
