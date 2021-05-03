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

@when("face your death", context="decision2")
def death_by_darkness():
  print(f" you chose to ignore the clown {name}. as you keep walking slowly a black void jumps around you. its coming in on all directions and slowly consumes you. and very soon you start to go insane and you commit suicide not to long later to escape the void. ")


@when("fight the clown", context="decision2")
def wise_but_do_you_have_what_it_takes():
  print(f" as you approach the clown {name} your worst fears begin to materialize as the clown instantly has access to the most powerful weapons you can imagine and as you try hard to give yourself weapons you realize you have a slim chance of surviving you shoot him in the head and the clown seems dead and you cried out in relief and you chose to change your dream environment to a better and more peaceful one. but what you did not notice is the clown is far from dead and is watching you this very moment. what will you do? wake up or think of a way to remove the clown from your dreams?")
