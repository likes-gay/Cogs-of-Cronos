import random
import json
import sys
import time
import os
from openai import OpenAI

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

def computer_select():
    return (getRandomPart("Head"), getRandomPart("Torso"), getRandomPart("Legs"))

def delete_last_x_lines(lines):
    for _ in range(lines):
        # Move the cursor up one line
        sys.stdout.write("\x1b[1A")
        # Clear the line
        sys.stdout.write("\x1b[2K")
    sys.stdout.flush()

def get_input(choices):
    while (user_input := input(f"\n{' '.join(choices)} >>> ")) not in choices:
        print("Invalid input. Please try again.")
        time.sleep(1)
        delete_last_x_lines(2)
        
    return user_input

def player_select(day, part_type):
    type(f"Welcome to day {day} of the scrapyard \n\n")
    time.sleep(.5)
    
    if day == 1:
        type("Here are the rules:\n")
        time.sleep(1.5)
        type("  * You can take home 1 part in this visit \n  * You can search up to 3 piles of scrap \n  * You can't go back to a pile you've already searched \n  * If you find a part you like, you can keep it but you will be unable to search the rest of the piles. \n\n")
        time.sleep(.5)
        print()
        
    else:
        type("The rules remain the same as your first visit\n")
    
    for i in range(1,3):
        type(f"Searching pile {i}")
        type(".")
        time.sleep(.2)
        type(".")
        time.sleep(.2)
        type(". \n")
        time.sleep(.2)
        time.sleep(1)
        part = getRandomPart(part_type)
        type(f"You found a {part['name']}!\n")
        time.sleep(0.5)
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


class GameAnalysis:
    def __init__(self, gh_token, player_name, player_parts, computer_parts):
        self.gh_token = gh_token
        self.client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=self.gh_token,
        )
        
        self.player_name = player_name
        self.player_parts = player_parts
        self.computer_parts = computer_parts
    
    def analyse_game_scores(self):
        def battle_log_entry(battle_winner, player_part, opponent_part):
            return {
                "battleWinner": battle_winner,
                "playerPart": player_part["name"],
                "opponentPart": opponent_part["name"],
                "roundDescription": self.analyse_round(player_part, opponent_part, battle_winner)
            }
        
        battle_log = []
        for i in range(3):
            random_player_part = random.choice(self.player_parts)
            random_computer_part = random.choice(self.computer_parts)
            
            if random.randint(1,2) == 1:
                # Player attacks
                
                if random_player_part["attack"] > random_computer_part["defence"]:
                    battle_log.append(battle_log_entry("player", random_player_part, random_computer_part))
                    
                else:
                    battle_log.append(battle_log_entry("computer", random_player_part, random_computer_part))
                
            else:
                # Computer attacks
                
                if random_computer_part["attack"] > random_player_part["defence"]:
                    battle_log.append(battle_log_entry("computer", random_player_part, random_computer_part))
                else:
                    battle_log.append(battle_log_entry("player", random_player_part, random_computer_part))
                    
        return battle_log
    
    def analyse_game_ai(self, battle_log):
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": '''
                    In user messages following, you will be provided with the player's part selection, the computer's part selection and a log of each part that was used in each round of the battle.
                    The battle round object will contain the winner of the round, the player's part and the computer's part.
                    If you are not provided with two json objects (one for the computer and one for the player) you must respond with an error message.
                    You must respond with a detailed description of how the parts used by each player in that round resulted in the outcomes of the battle log
                    Do not talk about other parts that were not used in that specific round.
                    Use the descriptions of the parts to make the battle more interesting.
                    In response to the user's messages you should provide the following:
                    OUTPUT IN VALID JSON (```python is not required) with keys "round1", "round2", "round3", each of these keys should hold a list of multiple strings, describing that round, make it exciting and dramatic!
                    Each entry in the round list should build suspense and excitement for the final outcome which should be the last entry in the list.
                    Use steam punk era terminology and descriptions
                   ''',
                },
                {
                    "role": "user",
                    "content": f"player_parts:{self.player_parts}, computer_parts:{self.computer_parts}, battle_log:{battle_log}",
                }
            ],
            model="gpt-4o-mini",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
        
        print(response.choices[0].message.content)
        
    def analyse_round(self, player_part, computer_part, battle_winner):
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": '''
                    In user messages following, you will be provided with the player's part selection, the computer's part selection and the outcome of the round.
                    The battle round object will contain the winner of the round, the player's part and the computer's part.
                    If you are not provided with the required objects you must respond with an error message.
                    
                    You must respond with a detailed description of how the parts used by each player in that round resulted in the outcomes of the battle log
                    Do not talk about other parts that were not used in that specific round.
                    Use the descriptions of the parts to make the battle more interesting.
                    In response to the user's messages you should provide the following:
                    
                    OUTPUT AS A VALID PYTHON LIST with [] brackets, containing multiple strings, describing that round, make it exciting and dramatic!
                    Ensure that the parts provided are used in the description.
                    the final list entry must show who won the round.
                    
                    '''
                },
                {
                    "role": "user",
                    "content": f"player_parts:{player_part}, computer_parts:{computer_part}, battle_winner:{battle_winner}",
                }
            ],
            model="gpt-4o-mini",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
        
        return(response.choices[0].message.content)
        
        
''' 
player_name = input("Enter your name: ")
player_parts = computer_select()
computer_parts = computer_select()

print(f"Player parts: {player_parts}")

print(f"Computer parts: {computer_parts}")

game_analysis = GameAnalysis(os.getenv("GH_TOKEN"), player_name, player_parts, computer_parts)
print(game_analysis.analyse_game_scores())

'''