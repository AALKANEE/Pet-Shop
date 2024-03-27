import json
import os.path

# inventory class
class inventory:
    pets={}

    def __init__(self):
        self.load()

#def: quantity(qty and q),key,value(v),file(f)
        
    def add(self,key,qty):
        q=0
        if key in self.pets:
            v=self.pets[key]
            q=v+qty
        else:
            q=qty
        self.pets[key]=q        
        print(f'Added {qty} {key}: total = {self.pets[key]}')

    def remove(self,key,qty):
        q=0
        if key in self.pets:
            v=self.pets[key]
            q=v-qty
        if q<0:
            q=0    
        self.pets[key]=q        
        print(f'Removed {qty} {key}: total = {self.pets[key]}')

    def display(self):
        for key, value in self.pets.items():
            print(f'{key} = {value}')

    def save(self):
        print('saving inventory')
        with open('inventory.txt', 'w') as f:
            json.dump(self.pets,f)
        print('Saving!')

    def load(self):
        print('Loading inventory')
        if not os.path.exists('inventory.txt'):
            print('Skipping,nothing to load')
            return
        with open('inventory.txt', 'r') as f:
            self.pets = json.load(f)
        print('Loaded!')