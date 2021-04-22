from adventurelib import *

def check_context(func):
  def inner():
    if get_context() == 'shoreline':
      func()
    else:
      print("You can't do that here.")
  return inner

set_context('shoreline')
print("Suddenly, your nostrils are filled with the strong scent of salt water as you realize you're on an island in the middle of the ocean.")

@when("stand up", context=('shoreline'))
def stand_up_shoreline():
  print("You stand up, causing the sand to shift beneath your feet.")

@when("sit down", context=('shoreline'))
def sit_down_shoreline():
  print("You sit down on the soft sand beneath you.")

@when("look around", context=('shoreline'))
def look_around_shoreline():
  print("You look around and notice a cave not too far from you.")

@when("enter the cave", context=('shoreline'))
def enter_cave():
  set_context('cave')
  print("You enter the cave.")

@when("look around", context=('cave'))
def look_around_cave():
  print("You look around and notice a sword on the ground.")

@when("stand up", context=('cave'))
def stand_up_cave():
  print("You stand up on the hard rock beneath you.")

@when("sit down", context=('cave'))
def sit_down_cave():
  print("You sit down on the hard rock beneath you.")

start()

