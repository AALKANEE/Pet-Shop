import json
import os.path

# inventory class
class inventory:
    pets={}

    def __init__(self):
        self.load()

#def add : quantity(qty and q),key,value(v)
    def add(self,key,qty):
        q=0
        if key in self.pets:
            v=self.pets[key]
            q=v+qty
        else:
            q=qty
        self.pets[key]=q        
        print(f'Added {qty} {key}: total = {self.pets[key]}')
    def remove(self):
        pass
    def display(self):
        pass
    def save(self):
        pass
    def load(self):
        pass