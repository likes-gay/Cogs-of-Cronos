import json
import random

points = 10

parts = json.load(open('robot.json'))
purchased_parts = []

def get_random_part():
    return random.choice(list(parts.keys()))

def get_part_not_purchased():
    part = get_random_part()
    while part in purchased_parts:
        part = get_random_part()
    return part

def part_selection_flow(points=10):
    parts_list = [get_part_not_purchased() for i in range(3)]
    parts_data = [parts[part] for part in parts_list]
    parts_names = [part['name'] for part in parts_data]

    print('Welcome to the Robot Battle!')
    print(f'You have {points} points to spend on parts for your robot.')
    print('Here are the available parts:', ", ".join(parts_names))


part_selection_flow()