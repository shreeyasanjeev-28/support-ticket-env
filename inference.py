import os
from openai import OpenAI
from env import SupportEnv, Action

client = OpenAI(
    api_key=os.environ.get("API_KEY"),
    base_url=os.environ.get("API_BASE_URL")
)

env = SupportEnv()

tasks = ["easy", "medium", "hard"]

for task_name in tasks:
    print(f"[START] task={task_name}", flush=True)

    obs = env.reset()

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": obs.ticket}
            ]
        )

        reply = response.choices[0].message.content

    except Exception as e:
        reply = "Sorry, we will resolve your issue shortly."

    action = Action(response=reply)

    obs, reward, done, info = env.step(action)

    print(f"[STEP] step=1 reward={reward}", flush=True)
    print(f"[END] task={task_name} score={reward} steps=1", flush=True)
