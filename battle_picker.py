import random
import json
import sys
import time

with open("./json_data/robot.json") as f:
    parts = json.load(f)

def type(text: str):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def getRandomPart(part_type):
    while True:
        random_part_key = random.choice(list(parts.keys()))
        
        if parts[random_part_key]["part"] == part_type:
            return parts[random_part_key]

def computerSelect():
    return (getRandomPart("Head"), getRandomPart("Torso"), getRandomPart("Legs"))

def delete_last_x_lines(lines):
    for _ in range(lines):
        # Move the cursor up one line
        sys.stdout.write("\x1b[1A")
        # Clear the line
        sys.stdout.write("\x1b[2K")
    sys.stdout.flush()

def get_input(choices):
    while (user_input := input("\n >>> ")) not in choices:
        print("Invalid input. Please try again.")
        time.sleep(1)
        delete_last_x_lines(2)
        
    return user_input

def playerSelect():
    type("Welcome to the scrapyard \n\n")
    time.sleep(.5)
    type("Here are the rules:\n")
    time.sleep(1.5)
    type("  * You can take home 1 part in this visit \n  * You can search up to 3 piles of scrap \n  * You can't go back to a pile you've already searched \n  * If you find a part you like, you can keep it but you will be unable to search the rest of the piles. \n\n")
    time.sleep(.5)
    type("")
    
    for i in range(1,3):
        type(f"Searching pile {i}")
        type(".")
        time.sleep(.2)
        type(".")
        time.sleep(.2)
        type(". \n")
        time.sleep(.2)
        time.sleep(1)
        part = getRandomPart("Head")
        type(f"You found a {part['name']}!\n")
        type(f"This is a '{part['desc']}'\n")
        
        type("Do you want to keep this part? (k/d)\n")
        match get_input(["k", "d"]):
            case "k":
                type(f"You picked up the {part['name']}. \n")
                return part
            case "d":
                continue
            case _:
                print("Invalid input. Defaulting to keep.")
        type("\n")
                
    type("You didn't pick up any parts. \n")
    return

print(playerSelect())
                
