from adventurelib import *
name=str(input("enter your name: "))
 
 run-down-bar = Room("""
After a long day of running errands and back-breaking tasks, you arrive at your apartment, ready for the great unwinding. After you put the tea on the stove, you take a nice, hot shower, shave, and prepare yourself for a night of relaxation and peace. A few hours pass by and soon you surrender to your fatigue. 

"Ay bartender, gimme two more of your strongest drinks"! 
"Yo Larry you sure you can handle another one, you look a bit sloshed mate"
"Ah shut up Oscar you posh brat"

Your eyes shoot open and there in your midst is... a stage and a bar?

"Lookie there guys... the slacker is finally awake" said a chubby guy wearing a checkered shirt and ripped jeans.
"He better be ready to produce the goods or else..." said another dressed in jet black.

Without a moment to waste, you are tied up from behind and dragged up to the elaborate and extensive cage on a stage. Thrust with a microphone and some water instructions are bellowed to you.

"Alright boy, listen here. Don't be nervous or your punishment will be severe. You have one task and that is all, its all on you whether you survive or fall. All we want to hear is a simple joke. Not corny, not silly, something witty and woke. And if you can get a sound out of us, we'll let you go without a fuss. "

"What do you do?"

"""))

@when("look around")
@when("stand up")
@when("crawl")
def look_around():
    print("You look around in your cage, the cold black bars looking right back at you")


@when("empty pockets")
def empty_pockets():
    print("You have leftover mentos and a paper that reads Don't be shy, come on out!")

@when("open door")
def cage_door():
    print("You crawl out of the cage, stretch, and start making your way around the bar")

@when("give ITEM to RECIPIENT")
def give(item, recipient):
    print("You give the {item} to the {recipient} and ask for some tips.")

item = "note"
recipient = "bartender"















start()

