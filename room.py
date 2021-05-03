
from adventurelib import *
name=str(input("enter your name: "))


room1 = Room("""You awake in a poorly lit and dark room. 

The only light is coming from the main door. An uneasy feeling has you overtaken. 
You are determined to get out of here.""")

room1.items=Bag()

hallway = Room("You walk through the door into a long hallay, with a series of doors on each side of the wall.")

current_room = room1



set_context("darkroom")

crowbar = Item('crowbar')

current_room.items.add(crowbar)






@when("look around", context='darkroom')
def look():
  print("The room is dark, and the only light is coming from the main door. You manage to notice a crowbar laying the floor")

@when("stand up", context='darkroom')
def stand_up():
  print("you stand up, although when you check what you were sitting on, nothing seems to be there.")

@when("inspect", context="darkroom")
def inspect():
  print("You inspect the walls closer, the color is black and rusty, strange material.") 
  

@when("take crowbar", context="darkroom")
def take():
  obj = current_room.items.take('crowbar')
  if not obj:
    print(f"You already have the crowbar.")
  else:
    print(f"You took the crowbar.")
    
    
@when("open door", context="darkroom")
def open():
  obj = current_room.items.take('crowbar')
  if not obj:
    print(f"With the help of your crowbar, you manage to open the door.")
    
  else:
    print(f"The door is blocked with two nailed in wooden pallets.")


