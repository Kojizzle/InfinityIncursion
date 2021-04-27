
from adventurelib import *
name=str(input("enter your name: "))


room1 = Room("""You awake in a poorly lit and dark room. 

The only light is coming from the main door. An uneasy feeling has you overtaken. 
You are determined to get out of here.""")

hallway = Room("You walk through the door into a long hallay, with a series of doors on each side of the wall.")

current_room = room1



set_context("darkroom")

crowbar = Item('crowbar')

current_room.items = crowbar




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
  def take(item):
    obj = current_room.items.take(item)
    if not obj:
      print(f"You already took the crowbar.")
    else:
      print(f"You took the {crowbar}.")
      inventory.add(obj)
    


