from adventurelib import *
from name import *

@when("run away", context="decision1")
def you_run_into_the_unknown():
  print("you quickly realize running is useless as all you see are more horrifying things around you until you faint and die. wake up wake up your dreaming")

@when("walk calmly", context="decision1")
def you_change_the_environment_around_you():
  set_context("creepy")
  print("as you convince yourself everything will be ok you notice the atmosphere around you changing to a more happy tone with good things happening around you it feels like time is flying as you have fun playing games at a carnival while also making friends. while you are blindly having fun a figure resembling a clown stands by the tree-line")

@when("approach the clown", context="creepy")
def fever_dream():
  set_context("decision2")
  print(f"as you approach the clown you see he slowly fades away while waving. but before he leaves he leaves a final message,{name} you will die tomorrow at 5pm. would you like to continue having fun or pursue the riddle?")
