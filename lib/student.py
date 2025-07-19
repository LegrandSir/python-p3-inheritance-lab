#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = knowledge
    
    def learn(self, info):
        self.knowledge.append(info)

    #def knowledge(self):
    