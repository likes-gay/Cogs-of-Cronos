import sys
import time
import os
from battle_picker import GameAnalysis, player_select, computer_select

print(os.getenv("GH_TOKEN"))

def large_title():
    print("""
░█▀▀█ █▀▀█ █▀▀▀ █▀▀ 　 █▀▀█ █▀▀ 　 ░█▀▀█ █──█ █▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀ 
░█─── █──█ █─▀█ ▀▀█ 　 █──█ █▀▀ 　 ░█─── █▀▀█ █▄▄▀ █──█ █──█ █──█ ▀▀█ 
░█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀ 　 ▀▀▀▀ ▀── 　 ░█▄▄█ ▀──▀ ▀─▀▀ ▀▀▀▀ ▀──▀ ▀▀▀▀ ▀▀▀
""")

def type(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def short_wait():
    time.sleep(1)
    print()
    
def pause():
    time.sleep(0.5)

def delete_last_x_lines(lines):
    for _ in range(lines):
        # Move the cursor up one line
        sys.stdout.write("\x1b[1A")
        # Clear the line
        sys.stdout.write("\x1b[2K")
    sys.stdout.flush()

def get_input(choices):
    time.sleep(2)
    print()
    while (user_input := input("\n >>> ")) not in choices:
        print("Invalid input. Please try again.")
        time.sleep(1)
        delete_last_x_lines(3)
        
    return user_input

large_title()
short_wait()

type("England, 1873.") 
short_wait()
type("Corruption has taken it's hold on the city of Belhelm, segregation between the classes of living through physical layers of the city, forcing the poorer population to live in filthy and crime filled streets, housing more citizens that it can handle.")
short_wait()
type("Homelessness, overpopulation, famine, problems affecting the lower class daily, causing violence and lawlessness to rise, striking fear into the innocent citizens that live below, whereas the upperclass get to live in luxury, thriving from the inequality.")
short_wait()
type("The city of Belhelm is a winding and complex structure, built from twisting layers that hold different economic classes, pressuring the less fortunate to work and live on the dirtier layers further down. The buildings are made from flimsy materials, -  ")
pause()
type("the streets covered in trash and slop from years of neglect from Belhelm's tyrant ruler, the population resorting to attacking and stealing from one another just to survive. Progressing, the quality of living increases as well, drastically changing- ")
pause()
type("toward the top, housing the richer and more important figures, including the ruler of the city herself. Their houses are luxurious, their streets are pristine with countless structures built lavishly, all achritectural marvels. ")
short_wait()
type("Despite the immense differences between the citizen classes, one thing remains the same; robot battling. Criminals, police officers, regular citizens, all owning and creating steam powered robots to fight alongside them for entertainment, commiting crimes-")
pause()
type("or upholding the law.")
short_wait()
type("A popular job on the lower layers are scrappers, a chance for the poorer citizens to earn the little money they need to survive. You happen to have been working as a scrapper for a few years, with access to the entire scrapyards inventory.")
short_wait()
short_wait()
type("Day 1...")
short_wait()
type("Talks of a revolution have been sparking up in the recent months, this is a chance for the lower class to fight against the tyranny that has been oppressing them daily. You being a citizen on the lowest level, are excited to join in.")
short_wait()
type("As you clock in to your job as a scrapper, you decide that if you want to fight back, you'll need to craft a robot for battling. Making your way to the piles of scrap, you look around for the coast to be clear... and begin.")

player_robot = []
player_robot.append(player_select(day=1, part_type="Torso"))
 
 
type("Day 2...")
short_wait()
type("Talks of the revolution are causing distress and excitement through the streets nearby. Your robot is coming along nicely, and your higherups do not suspect a thing.\n")
short_wait()
type("Clocking into work once more, you make your way to the scrap piles again... and begin.")
#Day 2
player_robot.append(player_select(day=2, part_type="Head"))
 
 
type("Day 3...")
short_wait()
type("Due to increased talks of the revolution, security and law enforcement around the lower layers of the city have increased, and suspense has reached an all time high.\n")
short_wait()
type("The robot you've been working on is almost at completetion, so for what you believe to be the last time, you step into work, and head for the scrap piles... to begin.")
#Day 3
player_robot.append(player_select(day=3, part_type="Legs"))
 

computer_robot = computer_select()


# Ask for user's robot name
robot_name = input("What would you like to name your robot? >>> ") 

battleAnalysis = GameAnalysis(os.getenv("GH_TOKEN"), robot_name, player_robot, computer_robot)

analysys = battleAnalysis.analyse_game_scores()

for i, entry in enumerate(analysys):

    type(f"---- ROUND {i+1} ----")
    print()
    entryDesc = entry["roundDescription"]
    
    type(entryDesc)
    short_wait()
    time.sleep(3)

type("-----------------------------")
short_wait()
print()
type("The overall winnner WAS!!!!")
type(analysys[0]["battleWinner"])

'''
type("With a big uproar, it seems as if the revolution has begun.")
type("After finally crafting your perfect robot, you're set to join the revolution and aid the cause of bringing down the tyrannical and corrupt ruling of the city of Belhelm.")
type("In the midst of the boom caused by the start of the revolution, you're able to sneak from your duty as a scrap worker, and take your crafted robot out of the scrapyard.")
#crossroad1 SCRAPYARD
type("As you step away from the scrapyard you're met with the cold and dirty streets, as well as a decision:    Do you march forward into the revolution(1)... or take a short detour back home before?(2)")

match get_input(["1","2"]):
         "1":
        #home
        type("You decide to take your usual, quick route back home, trudging along the damp, trash filled roads of the lowest layer of Belhelm.")
        type("Due to the uproar of the revolution and the familiarity of the path to your house, you're able to make it there in no time, stepping up to you(1)r front door.")
()2)
        
        match get_input(["1","2"]):
            case "1":
        
                type("Reaching for the flimsy door handle, you're interrupted by a commotion nearby. Sounds of a confrontation fill your ears:  Do you go to examine... or ignore it?")
                #home1.1: examine
                type("Following the sounds, you're met with the sight of a group of young revolutionists fighting a police officer in a losing battle. Quickly, help them!") #robot battle
                #after battle
            
            case "2":
        type("After a quick battle with the officer's robot you're thanked by the young group, and are able to return to your house shortly.")
                                #home1.2: ignore
        type("The sounds are an unnecessary distraction, and would take up time, so you decide to step straight into your home.")
    

        
        #into house 
        type("Stepping through the front door of your house, you're met with the familiar and warm atmosphere; despite it's decaying walls, cold and hard floor and chilly breeze throughout the rooms, you can't help but feel welcomed.")
        type("You search through the rooms, your eye finding a portrait of your late mother, the only remaining memory of the family you once had.")
type("With nothing else of value inside your house, you step back through your front door. It seems as if the conflict is over, so you make your way back to the scrapyard, the only way left forward.")
        
        #forward
        type("The sounds of the revolution echo through the lowest layer: metal crashing, steam hissing and distant screams. The path ahead will be long, but you're aware it's the necessary choice.")
        type("You're able to meet up with a few other revolutionists, all equipped with robots of their own.")
type("The evidence of conflict around is easily noticeable, rusty metal parts scattered all over, burn marks charring the concrete streets and buidlings relatively destroyed.")
        
        #barrier
        type("You and the group come across a line of law enforcement, their robots manned with weapons and defences. Each robot crafted with perfect welding and powerful offensive capabilities, perfect for keeping the streets 'safe' from criminals.")
        type("It's clear that they don't want you passing by, by the looks on their faces.")
type("Your friends prepare their robots, and with the help from them, you jump into battle with an officer!") #robot battle
        
        type("After a rough battle, you're able to sneak past alone, leaving the group in order to remain unseen.")
        type("Stepping carefully around, trying to avoid the gaze of anyone in your way, you're able to explore the now abandonded city streets.")
type("Soft chatter from hiding civilians fills your ears as you sneak around. The roads remain quiet other than the few revolutionists fixing up their battered robots. Curious to find the remaining mob, you approach a man sat on a bench, a sawblade in his hand.")
        
        #crossroad2 MAN ON STREET
        type("As you approach the man, he looks up, greeting you with a simple nod.")
        type("You reply with a simple nod, and a question.")
type("After asking your question the man responds with multiple directions, following three different groups he's seen: Do you take a left... continue forward... or take the right?")
        
        #Left
        type("After giving a small nod of thanks, you take a quick left into a slim alleyway, following trackmarks evident from a robot before.")
        type("You're able to quickly find the group of revolutionists the man before had mentioned. They're engaged in a battle with more law enforcement.")
        type("Gathering your bearings, you rush through and engage!") #robot battle
        type("Once more, you emerge victorious, and step back from the battered robots of the enemy, the officers fleeing all over.")
        type("Despite the victory, your robot is the only one standing, so after a thanks from the group, you leave once more, returning to the man.")
type("You notice the absence of the man, and the blockage of the road ahead. It seems the only way to go is to the right.")
        
        #forward
        type("After giving a small nod of thanks, you continue on the path forward.")
        type("As your distance from the man increases, it's eerily quiet, you're expecting to hear talking, battling, or even footsteps... but there's nothing.")
        type("You come across to the end of the street you're at, yet still noone's around.")
        type("Turning a corner, your eyes widen. You're met with the sight of a pile of battered robots. Approaching them, you're able to make out scorch marks, grated metal and deep cuts.")
        type("Despite the sad sight, some parts could come in handy, so you scavenge around for spare parts, adding, giving your robot some thicker defence.")
        type("After a few minutes, your robot looks much sturdier, so with a smile on your face you return to the man before.")
type("You notice the absence of the man, and the blockage of the alley to the left. It seems the only way to go is to the right.")

        
        #Right
        type("After giving a small nod of thanks, you take a quick right.")
        type("Before long, you realise you've found your way to the layer gate.")
        type("The gate is a massive mechanical door, a huge barrier preventing the lower classes from venturing above.")
        type("Around you are a large group of revolutionists and their impressive robots, all hissing and whirring as they battle with the opposing force. Metal crashes and screeches together causing a tense atmosphere of battle.")
        type("You take your step forward, rushing through the crowd, at the controls of the gate stands a tall and powerful robot, ready for fight. You look to your own, and confident with it's abilities, and fueled by the roars of battle around you. You engage.") #robot battle
        type("The battle was long, but you manage to emerge victorious.")
        type("You flick the switch to the gate, and with a large metallic screech, it opens for the first time in what seems to be years. The end of the tryanny seems to actually be close in grasp.")
        type("You step away from the controls, and followed by the large crowd, you charge to the layer above.")
type("END OF PROGLOGUE/CHAPTER 1")

        
'''