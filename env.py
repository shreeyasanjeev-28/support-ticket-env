from grader import grade_easy, grade_medium, grade_hard
from pydantic import BaseModel
from tasks import tasks
from grader import grade_response
import random

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
        self.current_task = None
        self.current_ticket = None
        self.history = []
        self.done = False

    # 🔁 Reset environment
    def reset(self):
       task = random.choice(tasks)

        self.current_task = task["type"]
        self.current_ticket = task["ticket"]
        self.current_grader = task["grader"]   
        
        self.history = []
        self.done = False
        
        return Observation(
            ticket=self.current_ticket,
            history=self.history
        )

    # ⚡ Step function
    def step(self, action: Action):
        if self.done:
            return (
                Observation(ticket=self.current_ticket, history=self.history),
                0.5,
                True,
                {"task_level": self.current_task}
            )

        # Add response to history
        self.history.append(action.response)

        reward = grade_response(action.response)
        
        # End after one step
        self.done = True

        return (
            Observation(ticket=self.current_ticket, history=self.history),
            reward,
            self.done,
            {"task_level": self.current_task}
        )

    # 📊 Current state
    def state(self):
        return {
            "ticket": self.current_ticket,
            "history": self.history,
            "done": self.done,
            "task_level": self.current_task
        }
