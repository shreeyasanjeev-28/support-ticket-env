import random
from pydantic import BaseModel
from tasks import tasks

# ✅ Observation model
class Observation(BaseModel):
    ticket: str
    history: list = []

# ✅ Action model
class Action(BaseModel):
    response: str

# ✅ Environment
class SupportEnv:
    def __init__(self):
        self.task = None
        self.current_ticket = None
        self.history = []
        self.done = False

    # 🔁 Reset
    def reset(self):
        self.task = random.choice(tasks)

        self.current_ticket = self.task["input"]
        self.history = []
        self.done = False

        return Observation(
            ticket=self.current_ticket,
            history=self.history
        )

    # ⚡ Step
    def step(self, action: Action):
        if self.done:
            return (
                Observation(ticket=self.current_ticket, history=self.history),
                0.5,
                True,
                {}
            )

        # Save response
        self.history.append(action.response)

        # ✅ CRITICAL: use grader directly from task
        reward = self.task["grader"](action.response)

        self.done = True

        return (
            Observation(ticket=self.current_ticket, history=self.history),
            reward,
            self.done,
            {}
        )

    # 📊 State
    def state(self):
        return {
            "ticket": self.current_ticket,
            "history": self.history,
            "done": self.done
        }
