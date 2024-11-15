import json
import sys
import time

mssgs = json.load(open('messages.json'))
robot = json.load(open('robot.json'))

def type(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)

type(mssgs['Welcome Screen'])

