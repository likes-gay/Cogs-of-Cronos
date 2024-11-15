import sys, time

def type(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)


def intro():
    type("Welcome to the game!\n")


import time

import pytermgui as ptg

typing = True
def create_msg_container(wholemg):
  global partmsg
  partmsg = ""
  def printmsg(arg):
    global partmsg

    time.sleep(0.08)
    if len(partmsg) < len(wholemg):
        partmsg = wholemg[:len(partmsg)+1]
        return partmsg
    
    else:
      typing = False
      return wholemg

  ptg.tim.define("!message", printmsg)

  return ptg.Container("[!message]%f", box="EMPTY")

def title():
  return ptg.Window("Welcome to the game!", box="DOUBLE")

with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    container1 = create_msg_container("""This is a message, with a type effect. 
    It will be displayed in a window. """)
    
    window1 = ptg.Window(title(), container1)
    
    manager.add(window1)