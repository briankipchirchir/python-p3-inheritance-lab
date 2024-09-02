#!/usr/bin/env python

from user import User

class Student(User):
    def _init_(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
        super()._init_(first_name,last_name)
        self.knowledge=[]
    
    def learn(self,new_knowlege):
        self.knowledge.append(new_knowlege)