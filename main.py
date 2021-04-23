from adventurelib import *

@when("look around")
def look():
  print("The room is dark, and the only light is coming from the main door.")

@when("stand up")
def stand_up():
  print("you stand up, although when you check what you were sitting on, nothing seems to be there.")

@when("inspect")
def inspect():
  print("You inspect the walls closer, the color is black and rusty, strange material.") 
  
    

start()

