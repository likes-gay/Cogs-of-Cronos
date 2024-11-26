import json
import random
import pytermgui as ptg
from partpicker_ui import part_picker
from part_manager import part_manager

points = 10

with open('robot.json') as f:
    parts = json.load(f)

def part_selection_flow(points=10):
    part_manager_instance = part_manager()

    print('Welcome to the Robot Battle!')
    print(f'You have {points} points to spend on parts for your robot.')


    manager = ptg.WindowManager()

    for i in range(3):
        part = part_manager_instance.get_part_not_purchased()
        window1 = part_picker(
            partID=part,
            name=part_manager_instance.parts[part]['name'],
            desc=part_manager_instance.parts[part]['desc'],
            attack=part_manager_instance.parts[part]['attack'],
            defence=part_manager_instance.parts[part]['defence'],
            cost=part_manager_instance.parts[part]['cost'],
            part=part,
            part_manager=part_manager_instance
        ).build_window()
    
        manager.add(window1)
    
    manager.run()

        

part_selection_flow()