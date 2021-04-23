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


""")

mark_corner = Room("""
Mark is chilling in the corner of the classroom as he usualy does. He is reading a book
""")

jess_hallway = Room("""
Entering the hallway, you see Jess quickly shut their bag. You thought you saw a glance ofsomething white and fluffy in the bag.

Jess: You didn't see anything!
""")

nightmare_hallway = Room("""

""")

nightmare_corner = Room("""

""")

nightmare_desk = Room("""

""")


ari = Item("ari")
ari.nightmare = False
ari.friend = False

jess = Item("jess")
jess.nightmare = False


mark = Item("mark")
mark.nightmare = False

current_room = your_desk
print(current_room)

@when("go to ari")
@when("walk to ari")
@when("go to aris desk")
@when("walk to aris desk")
def go_ari():
  if ari.nightmare == False:
    current_room = ari_desk
    print(current_room)

@when("go to mark")
@when("walk to mark")
@when("go to the corner")
@when("walk to the corner")
def go_mark():
  if mark.nightmare == False:
    current_room = mark_corner
    print(current_room)

@when("go to jess")
@when("walk to jess")
@when("go to the hallway")
@when("walk to the hallway")
@when("exit the classroom")
@when("exit the class")
@when("leave the classroom")
@when("leave the class")
def go_jess():
  if jess.nightmare == False:
    current_room = jess_hallway
    print(current_room)

@when("ask what is in the bag")
@when("ask jess what is in the bag")

start()

