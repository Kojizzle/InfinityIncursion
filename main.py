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

@when("stand up")
def stand_up():
  print("You stand up.")

@when("sit down")
def stand_up():
  print("You sit down.")

start()

