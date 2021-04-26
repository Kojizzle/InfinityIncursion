
from adventurelib import *
name=str(input("enter your name: "))



print("""You awake in a dark, poorly lit and dark room. 
The only light is coming from the main door. An uneasy feeling has you overtaken. 
You are determined to get out of here. """)


@when("look around")
def look():
  print("The room is dark, and the only light is coming from the main door. You manage to notice a crowbar laying the floor")

@when("stand up")
def stand_up():
  print("you stand up, although when you check what you were sitting on, nothing seems to be there.")

@when("inspect")
def inspect():
  print("You inspect the walls closer, the color is black and rusty, strange material.") 
  



