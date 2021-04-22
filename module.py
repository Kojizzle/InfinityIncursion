from adventurelib import *


@when("walk around", context="forest")
def walk():
  print("you stub your toe on a log.")

@when("look around", context="forest")
def explore():
  print("You see a dark forest, filled with the sounds of wildlife.")