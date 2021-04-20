from adventurelib import *
from module import *

@when("look around")
def look():
  print("you look around")

@when("pick up a thing")
def look():
  print("you pick it up")

@when("stand up")
def look():
  print("you stand up")

@when("walk outside")
def go_outside():
  set_context("outside")
  print("You walk outside")

start()

