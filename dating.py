from adventurelib import *
from name import *

set_context('your_desk')
your_desk = Room("""
You are at your desk in the classroom. Class has ended and everyone is either about to go home or is preparing for aftershool activities.

You see your friend Mark sitting in the corner of the classroom reading a book. He is wearing his usual grey sweatshirt, despite the temperature in the building being fairly warm.

You see your friend Jess walk outside the classroom and enter the hallway. They are holding onto their bag, but you know that they hang out in the hallway afterschool instead of going home right away.

You see a new student sitting at a desk close to yours. If you remember correctly, the teacher said her name was Ari.

You feel compelled to start getting closer to one of your fellow classmates. 

What do you do?
""")

ari_desk = Room("""
Ari is sitting at her desk, she has long brown hair with a pink streak in it. It looks like she is stuggling with some of the homework she was given for math class.

ARI: Oh! Sorry, I didn't see you there. Do you need help or something?
""")

mark_corner = Room("""
Mark is chilling in the corner of the classroom as he usualy does. He is reading a book with a solid black cover.
""")

jess_hallway = Room("""
Entering the hallway, you see Jess in their loose and baggy clothing quickly shut their bag. You thought you saw a glance of something white and fluffy in the bag.

JESS: You didn't see anything!
""")

ari_win = Room("""
You and Ari have forged a bond of Friendship!
""")

mark_win = Room("""
You and Mark have deepened your bond!
""")

jess_win = Room("""
You and Jess have deepened your bond!
""")

nightmare_desk = Room("""
The area around the desks starts to become oddly geometric, with sudden angles and geometric faces emerging out of nowhere. Ari then starts to convulse as her limbs extend and contort as she becomes more angular in appearence, with her head becoming the shape of a nonogon.
""")

nightmare_hallway = Room("""
The hallway outside the classroom bends and warps in unusual ways, as Jess' body contorts and bends. Their body becomes that of a tall and gaunt pale figure, with a large, pale, furry beast with yellowed gnashing teeth and several clouded eyes growing out of their side. A bag you know as once belonging to Jess rests at the new creatures feet. 
""")

nightmare_corner = Room("""
Nightmare Mark is a work in progress, but it's responce is still operational.
""")

ari_terror = Room("""
You have now become a part of the nonogon horror!!!
""")

mark_terror = Room("""
You and Mark are no longer as close of friends!!!
""")

jess_terror = Room("""
You have been consumed by the entity once known as Jess!!!
""")

ari = Item("ari")
ari.nightmare = False
ari.helpless = True
ari.stumped = True
ari.merge = False

jess = Item("jess")
jess.nightmare = False
jess.fluff = False
jess.pleased = False
jess.angered = False

mark = Item("mark")
mark.nightmare = False
mark.book = False
mark.sad = True
mark.night = True

current_room = your_desk
print(current_room)

@when("do nothing", context=('your_desk'))
def oh_no():
  print("you will regret this")
  ari.nightmare = True
  jess.nightmare = True
  

@when("go to ari", context='your_desk')
@when("walk to ari", context='your_desk')
@when("go to aris desk", context='your_desk')
@when("walk to aris desk", context='your_desk')
def go_ari():
  global current_room
  if ari.nightmare == False:
    current_room = ari_desk
    set_context('ari_desk')
    print(current_room)
  else:
    current_room = nightmare_desk
    print(current_room)
    set_context('ari_desk')

@when("ask ari if she needs help", context='ari_desk')
@when("ask her if she needs help", context='ari_desk')
@when("ask if she needs help", context='ari_desk')
def ask_ari():
  global current_room
  if current_room == ari_desk:
    print("Ari looks suprised when you ask if she needs help. ARI: Oh! Well, I do need help actualy, I'm working on some geometry homework, but I am horible at math. Can you take a look at this?  She shows you the problem in the textbook: 8=8(x-8) find x.")
    ari.helpless = False
    set_context('ari_math')
  elif current_room == nightmare_desk:
    print(f"ARI: I am perfectly fine {name}. All nine of my sides are together in perfect harmony. Do you wish to join us {name}?")
    set_context('ari_math')
    ari.helpless = False
  else:
    print("Ari isn't here!")

@when("the answer is nine", context='ari_math')
@when("nine", context='ari_math')
def math_ari():
  global current_room
  if current_room == ari_desk:
    print(f"ARI: Oh! So it is! Thanks for the help {name}!")
    current_room = ari_win
    print(current_room)
    set_context('ari_win')
  elif current_room == nightmare_desk:
    print(f"ARI: {name}! You are now one of my nine sides!")
    current_room = ari_terror
    print(current_room)
    set_context('ari_terror')
  else:
    print("Ari isn't here!")

@when("i dont know", context='ari_math')
def wrong_ari():
  global current_room
  if current_room == ari_desk:
    print("Ari looks disapointed. ARI: Oh, well that's a shame...")
    ari.nightmare = True
    current_room = nightmare_desk
    print(current_room)
    set_context('ari_desk')
  elif current_room == nightmare_desk:
    print(f"ARI: {name}! You are now one of my nine sides!")
    current_room = ari_terror
    print(current_room)
    set_context('ari_terror')
  else:
    print("Ari isn't here!")



@when("go to jess", context='your_desk')
@when("walk to jess", context='your_desk')
@when("go to the hallway", context='your_desk')
@when("walk to the hallway", context='your_desk')
@when("exit the classroom", context='your_desk')
@when("exit the class", context='your_desk')
@when("leave the classroom", context='your_desk')
@when("leave the class", context='your_desk')
def go_jess():
  global current_room
  if jess.nightmare == False:
    current_room = jess_hallway
    print(current_room)
    set_context('jess_hallway')
  else: 
    current_room = nightmare_hallway
    set_context('jess_hallway')
    print(current_room)

@when("ask what is in the bag", context='jess_hallway')
@when("ask them what is in the bag", context='jess_hallway')
@when("ask jess what is in the bag", context='jess_hallway')
@when("ask what was in the bag", context='jess_hallway')
@when("ask them was in the bag", context='jess_hallway')
@when("ask jess what was in the bag", context='jess_hallway')
def ask_jess():
  global current_room
  if current_room == jess_hallway:
    print(f"JESS: {name} I swear, if you tell ANYONE, I will end you!" + 
    "They open their bag and show you a little white mouse with beady little eyes." + "JESS: I found him in the trash and I thought that he was too cute to just ignore, what do you think of him?")
    jess.fluff = True
    set_context('jess_fluff')
  elif current_room == nightmare_hallway:
    print(f" The being once known as Jess speaks from their gnashing toothy maw. JESS: {name}! There is no bag {name}! We are many {name}! What do you think of us {name}?")
    jess.fluff = True
    set_context('jess_fluff')
  else:
    print("Jess and their bag aren't here!")

@when("tell them you think the mouse is cute", context='jess_fluff')
@when("tell jess you think the mouse is cute", context='jess_fluff')
@when("you think he is cute", context='jess_fluff')
@when("you think they are cute", context='jess_fluff')
def cute_jess():
  global current_room
  if current_room == jess_hallway:
    print(f"Jess seems very glad that you like her new friend. JESS: Great! So that means you won't report us to the administration, right {name}?")
    set_context('jess_win')
    current_room = jess_win
  elif current_room == nightmare_hallway:
    print(f"The mawed creature surrounds you...")
    set_context('jess_terror')
    current_room = jess_terror
    print(current_room)
  else:
    print("Jess and their bag aren't here!")

@when("tell them you think the mouse is ugly", context='jess_fluff')
@when("tell jess you think the mouse is ugly", context='jess_fluff')
@when("you think the mouse is ugly", context='jess_fluff')
@when("you think they are ugly", context='jess_fluff')
@when("you think they are scary", context='jess_fluff')
def ugly_jess():
  global current_room
  if current_room == jess_hallway:
    print(f"You didn't have to be rude about it {name}!")
    jess.nightmare = True
    current_room = nightmare_hallway
    print(current_room)
    set_context('jess_hallway')
  elif current_room == nightmare_hallway:
    print(f"The mawed creature surrounds you...")
    current_room = jess_terror
    print(current_room)
    set_context('jess_terror')
  else:
    print("Jess isn't here!")


@when("go to mark", context='your_desk')
@when("walk to mark", context='your_desk')
@when("go to the corner", context='your_desk')
@when("walk to the corner", context='your_desk')
def go_mark():
  global current_room
  if mark.nightmare == False:
    current_room = mark_corner
    print(current_room)
    set_context('mark_corner')
  else:
    current_room = nightmare_corner
    print(current_room)

@when("ask mark what he is reading", context='mark_corner')
@when("ask him what he is reading", context='mark_corner')
@when("ask what he is reading", context='mark_corner')
def ask_mark():
  global current_room
  if current_room == mark_corner:
    print(f"Mark looks up from his book. MARK: Oh hey! I'm just reading this stupid book for my English class. I need to get my mind of this book. Hey {name}, would you rather play sports or read books?")
    mark.book = True
    set_context('mark_question')
  elif current_room == nightmare_corner:
    print("wip nightmare mark")
    mark.book = True
    set_context('mark_question')
  else:
    print("Mark isn't here!")

@when("you like sports more than reading", context='mark_question')
def sports_mark():
  global current_room
  if current_room == mark_corner:
    print(f"Hell yeah {name}! I can read this later, let's go down to the track and do something else.")
    current_room = mark_win
    set_context('mark_win')
    print(current_room)
  else:
    print("Mark isn't here!")

@when("you like reading more than sports", context='mark_question')
def sports_mark():
  global current_room
  if current_room == mark_corner:
    print(f"Oh. Really? Man I totaly thought you liked sports more...")
    mark.nightmare = True
    current_room = mark_terror
    print(current_room)
    set_context('mark_terror')
  else:
    print("Mark isn't here!")


@when("return to lobby", context='ari_win')
def ari_win_return():
  set_context('lobby')
  current_room = lobby 

@when("return to lobby", context='jess_win')
def jess_win_return():
  set_context('lobby')
  current_room = lobby 

@when("return to lobby", context='mark_win')
def mark_win_return():
  set_context('lobby')
  current_room = lobby 

@when("return to lobby", context='ari_terror')
def ari_terror_return():
  set_context('lobby')
  current_room = lobby 

@when("return to lobby", context='jess_terror')
def jess_terror_return():
  set_context('lobby')
  current_room = lobby 

@when("return to lobby", context='mark_terror')
def mark_terror_return():
  set_context('lobby')
  current_room = lobby 

