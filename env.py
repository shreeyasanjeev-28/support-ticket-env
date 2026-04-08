from pydantic import BaseModel
from typing import Tuple
from tasks import TASKS
from grader import grade
import random

class Observation(BaseModel):
    ticket: str
    history: list[str]

class Action(BaseModel):
    response: str

class SupportEnv:
    def __init__(self):
        self.current_task = None
        self.done = False

    def reset(self):
        self.current_task = random.choice(TASKS)
        self.done = False
        return Observation(
            ticket=self.current_task["ticket"],
            history=[]
        )

    def step(self, action: Action) -> Tuple[Observation, float, bool, dict]:
        score = grade(action.response, self.current_task["expected_keywords"])

        reward = score

        # penalty for bad/short responses
        if len(action.response.strip()) < 5:
            reward -= 0.2

        self.done = True

        return (
            Observation(ticket="", history=[]),
            reward,
            self.done,
            {"task_level": self.current_task["level"]}
        )

    def state(self):
        return self.current_task