import random
import json
import sys
import time

with open("./json_data/robot.json") as f:
    parts = json.load(f)

def type(text):
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


def playerSelect():
    type("Welcome to the scrapyard. You can search up to 3 piles of scrap, but you can't go back to a pile you've already searched.\n")
    time.sleep(1)
    
    parts = []
    
    for i in range(1,3):
        type(f"Searching pile {i}...\n")
        time.sleep(1)
        part = getRandomPart("Head")
        type(f"You found a {part['name']}!\n")
        
        match input("Keep or discard? (k/d): ").lower():
            case "k":
                parts.append(part)
                break
            case "d":
                continue
            case _:
                print("Invalid input. Defaulting to keep.")
                parts.append(part)
                break
    