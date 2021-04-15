from adventurelib import *

@when("look around")
def look():
  print("you look around")

@when("stand up")
def look():
  print("you stand up")

start()

@when("walk around")
def open():
  print("you walk around for a while")