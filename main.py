from story import large_title, short_wait, scene_0, scene_1, scene_2, scene_3, type
import random
import os
from dotenv import load_dotenv


num_cogs = random.randint(10, 30)

# Get the GitHub token from the environment for use with the GitHub Models API
load_dotenv()
GH_TOKEN = os.getenv('GH_TOKEN')
if not GH_TOKEN:
    GH_TOKEN = input("Please enter your GitHub token: ")
    with open('.env', 'a') as f:
        f.write(f'GH_TOKEN={GH_TOKEN}')
    
large_title()
short_wait()
scene_0()
type(f"Starting funds: ⚙ {num_cogs}")
short_wait()
scene_1()

#TODO, implement random part picking for scene 2
scene_2()
scene_3()