import os
from env import SupportEnv, Action

env = SupportEnv()

obs = env.reset()

print("Ticket:", obs.ticket)

# Simulated response instead of API
if "order" in obs.ticket.lower():
    reply = "Sorry for the inconvenience. I will track your order and update you."
elif "damaged" in obs.ticket.lower():
    reply = "Sorry for the issue. We can offer a refund or replacement for the damaged product."
elif "charged" in obs.ticket.lower():
    reply = "We apologize. We will refund the extra charge and escalate this issue as priority."
else:
    reply = "Sorry, we will look into this issue."
print("Model Response:", reply)

action = Action(response=reply)

obs, reward, done, info = env.step(action)

print("Reward:", reward)
print("Task Level:", info["task_level"])