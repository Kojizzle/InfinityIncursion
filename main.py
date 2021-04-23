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
  print("you look into the mirror and see a twisted and contorted version of yourself that sends chills down your spine then it fades away you have a choice to panic and run or keep walking calmly in this bizarre world")  



start()

