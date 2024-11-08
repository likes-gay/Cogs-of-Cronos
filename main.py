import sys, time

def type(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)


def intro():
    type("Welcome to the game!\n")