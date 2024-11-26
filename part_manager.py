import json
import random

class part_manager():
    def __init__(self):
        with open('robot.json') as f:
            self.parts = json.load(f)
        self.purchased_parts = []
        self.points = 10

    def get_random_part(self):
        return random.choice(list(self.parts.keys()))
    
    def purchase_part(self, part):
        self.purchased_parts.append(part)
        self.points -= int(self.parts[part]['cost'])
    
    def get_balance(self):
        return self.points
    
    def get_part_not_purchased(self):
        part = self.get_random_part()
        while part in self.purchased_parts:
            part = self.get_random_part()
        return part
    