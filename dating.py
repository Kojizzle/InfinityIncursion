from adventurelib import *

your_desk = Room("""
You are at your desk in the classroom. Class has ended and everyone is either about to go home or is preparing for aftershool activities.

You see your friend Mark sitting in the corner of the classroom reading a book. He is wearing his usual grey sweatshirt, despite the temperature in the building being fairly warm.

You see your friend Jess walk outside the classroom and enter the hallway. They are holding onto their bag, but you know that they hang out in the hallway afterschool instead of going home right away.

You see a new student sitting at a desk close to yours. If you remember correctly, the teacher said her name was Ari.

You feel compelled to start getting closer to one of your fellow classmates. 

What do you do?
""")

ari_desk = Room("""

""")

mark_corner = Room("""

""")

jess_hallway = Room("""

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


start()

