from adventurelib import *

@when("look around")
def look():
  print("you look around")

@when("stand up")
def look():
  print("you stand up")

start()

@when("open your eyes")
def open_eyes():
  say("""Your eyes open, you aren't in your bedroom anymore...
  """)