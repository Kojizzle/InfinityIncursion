from adventurelib import *
from reactions import *
from name import *


@when("look around")
def look():
  print("you look around")

@when("stand up")
def stand_up():
  print("you stand up")

@when("walk around")
def walk_around():
  print("you walk around looking for something and you notice yourself in a strange other-worldly dimension. you look up and see other planets very close and 4 red suns")  

@when("realize")
def realize():
  print("you realize you are in a dream you can control")


@when("look at the mirror")
def mirrored_horror():
  set_context("decision1")
  print("you look into the mirror and see a twisted and contorted version of yourself that sends chills down your spine then it fades away you have a choice to panic and run or keep walking calmly in this bizarre world")  

@when("keep having fun", context="decision2")
def buissness_before_pleasure_peasant():
  print(f"you decide to ignore the riddle and keep having fun until you get awoken in the real world just to see that same clown in real life. he shouts your name {name}, you shall die for your ignorance. startled you get up and run but he quickly responds and snaps your neck. is this a dream? im afraid not")

@when("follow the riddle",context="decision2")
def wise_choice_peasant():
  print(f"you deicde to think about what the clown said and all of a sudden the world around you starts to shift into a new reality where you can spawn anything you want but a warning in the sky shows a startling message {name} will die tomorrow by 5pm. to prevent this you must kill the clown.")



start()
