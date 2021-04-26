from adventurelib import *
from horror import *

@when("look around")
def look():
  print("you look around")

@when("stand up")
def stand_up():
  print("you stand up")

@when("walk around")
def walk_around():
  print("you walk around looking for something")  

start()

