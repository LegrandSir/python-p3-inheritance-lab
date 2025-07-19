# teacher.py
from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "Variables store values",
            "Loops help automate repetitive tasks",
            "Functions encapsulate logic",
            "Classes define object blueprints"
        ]

    def teach(self):
        return random.choice(self.knowledge)
