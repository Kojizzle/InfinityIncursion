from adventurelib import *


set_context('shoreline')
print("Suddenly, your nostrils are filled with the strong scent of salt water as you realize you're on an island in the middle of the ocean.")

@when("stand up", context='shoreline')
def stand_up_shoreline():
  print("You stand up, causing the sand to shift beneath your feet.")

@when("sit down", context='shoreline')
def sit_down_shoreline():
  print("You sit down on the soft sand beneath you.")

@when("look around", context='shoreline')
def look_around_shoreline():
  print("You look around and see a cave not too far from you.")

@when("enter the cave", context='shoreline')
def enter_cave():
  set_context('cave')
  print("You enter the cave.")

@when("look around", context='cave')
def look_around_cave():
  print("You look around and notice a sword on the ground.")

@when("stand up", context='cave')
def stand_up_cave():
  print("You stand up on the hard rock beneath you.")

@when("sit down", context='cave')
def sit_down_cave():
  print("You sit down on the hard rock beneath you.")

@when("take the sword", context='cave')
def take_sword():
  set_context('attack')
  print("You walk over and grab the sword. Suddenly, you hear footsteps behind you. As you turn around with the sword in hand, a black figure lunges at you. You have two options, try to dodge or swing your sword at it.")

@when("dodge", context='attack')
def dodge_attack():
  set_context('shoreline')
  print("You dodge the figure's attack and run back outside with the sword in hand.")

@when("swing sword", context='attack')
def swing_sword():
  set_context('???')
  print("You swing your sword, hitting it directly. However, the sword doesn't phase it and... (?)")

