import os
from openai import OpenAI
from env import SupportEnv, Action

# REQUIRED ENV VARIABLES (STRICT)
API_BASE_URL = os.environ["API_BASE_URL"]
API_KEY = os.environ["API_KEY"]
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

# CLIENT USING THEIR PROXY
client = OpenAI(
    api_key=API_KEY,
    base_url=API_BASE_URL
)

env = SupportEnv()
obs = env.reset()

ticket = obs.ticket

# DETERMINE TASK
if "order" in ticket.lower():
    task = "easy"
elif "damaged" in ticket.lower():
    task = "medium"
elif "charged" in ticket.lower() or "billing" in ticket.lower():
    task = "hard"
else:
    task = "unknown"

# REQUIRED STRUCTURED OUTPUT
print(f"[START] task={task}", flush=True)

# REAL LLM CALL (THIS FIXES YOUR ERROR)
response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": "You are a helpful customer support assistant."},
        {"role": "user", "content": ticket}
    ]
)

reply = response.choices[0].message.content

action = Action(response=reply)
obs, reward, done, info = env.step(action)

print(f"[STEP] step=1 reward={reward}", flush=True)
print(f"[END] task={task} score={reward} steps=1", flush=True)
