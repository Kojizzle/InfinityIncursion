from adventurelib import *


set_context('shoreline')
print("""Suddenly, your nostrils are filled with the strong scent of salt water as you realize you're on an island in the middle of the ocean.""")

@when("stand up", context='shoreline')
def stand_up_shoreline():
  print("""You stand up, causing the sand to shift beneath your feet.""")

@when("sit down", context='shoreline')
def sit_down_shoreline():
  print("""You sit down on the soft sand beneath you.""")

@when("look around", context='shoreline')
def look_around_shoreline():
  print("""You look around through thick fog and barely manage to make out a cave not too far from you.""")

@when("enter the cave", context='shoreline')
def enter_cave():
  set_context('cave')
  print("""You enter the cave.""")

@when("look around", context='cave')
def look_around_cave():
  print("""You look around and notice a sword on the ground.""")

@when("stand up", context='cave')
def stand_up_cave():
  print("""You stand up on the hard rock beneath you.""")

@when("sit down", context='cave')
def sit_down_cave():
  print("""You sit down on the hard rock beneath you.""")

@when("take the sword", context='cave')
def take_sword():
  set_context('attack')
  print("""You walk over and grab the sword. Suddenly, you hear footsteps behind you. As you turn around with the sword in hand, a black figure lunges at you. You have two options, try to dodge or swing your sword at it.""")

@when("dodge", context='attack')
def dodge_attack():
  set_context('shoreline2')
  print("""You dodge the figure's attack and run back outside with the sword in hand.""")

@when("swing sword", context='attack')
def swing_sword():
  set_context('???')
  print("""You swing your sword, hitting it directly. However, the sword doesn't phase it and it hits you, causing everything to go black.""")

@when("stand up", context='shoreline2')
def stand_up_shoreline():
  print("""You stand up, causing the sand to shift beneath your feet.""")

@when("sit down", context='shoreline2')
def sit_down_shoreline():
  print("""You sit down on the soft sand beneath you.""")

@when("look around", context='shoreline2')
def look_around_shoreline():
  print("""You look around and see the cave you just ran from not too far from you. You also see a mountain that was wasn't visible beforehand due to the fog. You see a pathway leading to the top that you can use to climb the mountain.""")

@when("climb the mountain", context='shoreline2')
def climb_mountain():
  set_context('mountainpathway')
  print("""You start to climb the mountain, but halfway up the pathway when you hear loud cracking up above you. You look up to see a big boulder hurtiling towards you, but you can't tell where it's exactly going to land. You can either dodge forward or dodge backwards.""")

@when("dodge forward", context='mountainpathway')
def dodge_forward():
  set_context('death')
  print("""You dodged the wrong way and were crushed by the boulder.""")

@when("dodge backward", context='mountainpathway')
def dodge_backward():
  set_context('blocked')
  print("""You just managed to dodge the boulder as it lands with a big crack in front of you, but your pathway is now blocked.""")

@when("walk down the mountain", context='blocked')
def down_mountain():
  set_context('shoreline3')
  print("""You walk down the mountain back down to the shoreline.""")

@when("stand up", context='shoreline3')
def stand_up_shoreline():
  print("""You stand up, causing the sand to shift beneath your feet.""")

@when("sit down", context='shoreline3')
def sit_down_shoreline():
  print("""You sit down on the soft sand beneath you.""")

@when("look around", context='shoreline3')
def look_around():
  print("""You look around at the environment surrounding you, but you feel hungry an thirsty. You notice a nearby tree with some fruit hanging off of it.""")

@when("walk to tree", context='shoreline3')
def walk_tree():
  set_context('banana tree')
  print("""You walk over to the tree to identify that the fruit's on the tree are bananas. However, you'd have to climb the tree to reach them.""")

@when("climb the tree", context='banana tree')
def climb_tree():
  set_context('???')
  print("""You start the climb the tree, making it pretty far, but as you're climbing the tree one of the branches you grab on to suddenly snaps. You fall to the ground expecting to be met with pain but you instead keep on falling into the abyss. """)