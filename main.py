from adventurelib import *
from dating import *
@when("look around")
def look():
  print("you look around")

@when("stand up")
def stand_up():
  print("you stand up")

@when("open your eyes")
def open_eyes():
  say("""Your eyes open, you aren't in your bedroom anymore...
  """)


start()

