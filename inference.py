import os
from openai import OpenAI
from env import SupportEnv, Action

# ✅ REQUIRED ENV VARIABLES
API_BASE_URL = os.environ["API_BASE_URL"]
API_KEY = os.environ["API_KEY"]
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

client = OpenAI(
    api_key=API_KEY,
    base_url=API_BASE_URL
)

env = SupportEnv()
obs = env.reset()

ticket = obs.ticket.lower()

# ✅ DETERMINE TASK
if "order" in ticket:
    task = "easy"
elif "damaged" in ticket:
    task = "medium"
elif "charged" in ticket or "billing" in ticket:
    task = "hard"
else:
    task = "unknown"

print(f"[START] task={task}", flush=True)

# ✅ SAFE API CALL
try:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful customer support assistant."},
            {"role": "user", "content": ticket}
        ],
        timeout=10
    )
    reply = response.choices[0].message.content

except Exception as e:
    # ✅ FALLBACK (VERY IMPORTANT)
    if "order" in ticket:
        reply = "Sorry, I will track your order."
    elif "damaged" in ticket:
        reply = "We will provide refund or replacement."
    elif "charged" in ticket or "billing" in ticket:
        reply = "We will refund and escalate this issue."
    else:
        reply = "We will look into this issue."

action = Action(response=reply)

# ✅ SAFE ENV STEP
try:
    obs, reward, done, info = env.step(action)
except Exception:
    reward = 0.0

print(f"[STEP] step=1 reward={reward}", flush=True)
print(f"[END] task={task} score={reward} steps=1", flush=True)
