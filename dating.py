from adventurelib import *
name=str(input("enter your name: "))

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

nightmare_desk = Room("""
The area around the desks starts to become oddly geometric, with sudden angles and geometric faces emerging out of nowhere. Ari then starts to convulse as her limbs extend and contort as she becomes more angular in appearence, with her head becoming the shape of a nonogon.
""")

nightmare_hallway = Room("""
The hallway outside the classroom bends and warps in unusual ways, as Jess' body contorts and bends. Their body becomes that of a tall and gaunt pale figure, with a large, pale, furry beast with yellowed gnashing teeth and several clouded eyes growing out of their side. A bag you know as once belonging to Jess rests at the new creatures feet. 
""")

nightmare_corner = Room("""
Nightmare Mark is a work in progress, but it's responce is still operational.
""")

ari = Item("ari")
ari.nightmare = False
ari.helpless = True
ari.stumped = True

jess = Item("jess")
jess.nightmare = False
jess.fluff = False

mark = Item("mark")
mark.nightmare = False
mark.book = False
mark.sad = True

current_room = your_desk
print(current_room)

@when("do nothing")
def oh_no():
  print("you will regret this")
  ari.nightmare = True
  jess.nightmare = True
  mark.nightmare = True

@when("go to ari")
@when("walk to ari")
@when("go to aris desk")
@when("walk to aris desk")
def go_ari():
  global current_room
  if ari.nightmare == False:
    current_room = ari_desk
    print(current_room)
  else:
    current_room = nightmare_desk
    print(current_room)

@when("ask ari if she needs help")
@when("ask her if she needs help")
@when("ask if she needs help")
def ask_ari():
  global current_room
  if current_room == ari_desk:
    print("Ari looks suprised when you ask if she needs help. ARI: Oh! Well, I do need help actualy, I'm working on some geometry homework, but I am horible at math. Can you take a look at this?  She shows you the problem in the textbook.")
    ari.helpless = False
  elif current_room == nightmare_desk:
    print(f"ARI: I am perfectly fine {name}. All nine of my sides are together in perfect harmony. Do you wish to join us {name}?")
    ari.helpless = False
  else:
    print("Ari isn't here!")


@when("go to jess")
@when("walk to jess")
@when("go to the hallway")
@when("walk to the hallway")
@when("exit the classroom")
@when("exit the class")
@when("leave the classroom")
@when("leave the class")
def go_jess():
  global current_room
  if jess.nightmare == False:
    current_room = jess_hallway
    print(current_room)
  else: 
    current_room = nightmare_hallway
    print(current_room)

@when("ask what is in the bag")
@when("ask them what is in the bag")
@when("ask jess what is in the bag")
@when("ask what was in the bag")
@when("ask them was in the bag")
@when("ask jess what was in the bag")
def ask_jess():
  global current_room
  if current_room == jess_hallway:
    print(f"JESS: {name} I swear, if you tell ANYONE, I will end you!" + 
    "They open their bag and show you a little white mouse with beady little eyes." + "JESS: I found him in the trash and I thought that he was too cute to just ignore, what do you think of him?")
    jess.fluff = True
  elif current_room == nightmare_hallway:
    print(f" The being once known as Jess speaks from their gnashing toothy maw. JESS: {name}! There is no bag {name}! We are many {name}! What do you think of us {name}?")
    jess.fluff = True
  else:
    print("Jess and their bag aren't here!")


@when("go to mark")
@when("walk to mark")
@when("go to the corner")
@when("walk to the corner")
def go_mark():
  global current_room
  if mark.nightmare == False:
    current_room = mark_corner
    print(current_room)
  else:
    current_room = nightmare_corner
    print(current_room)

@when("ask mark what he is reading")
@when("ask him what he is reading")
@when("ask what he is reading")
def ask_mark():
  global current_room
  if current_room == mark_corner:
    print("wip mark")
    mark.book = True
  elif current_room == nightmare_corner:
    print("wip nightmare mark")
    mark.book = True
  else:
    print("Mark isn't here!")


start()

