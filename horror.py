from adventurelib import *
from reactions import *
from name import *

set_context("startgame")

@when("look around", context="startgame")
def look():
  print("you look around")

@when("stand up", context="startgame")
def stand_up():
  print("you stand up")

@when("walk around", context="startgame")
def walk_around():
  print("you walk around looking for something and you notice yourself in a strange other-worldly dimension. you look up and see other planets very close and 4 red suns")  

@when("realize", context="startgame")
def realize():
  print("you realize you are in a dream you can control")


@when("look at the mirror", context="startgame")
def mirrored_horror():
  set_context("decision1")
  print("you look into the mirror and see a twisted and contorted version of yourself that sends chills down your spine then it fades away you have a choice to panic and run or keep walking calmly in this bizarre world")  

@when("keep having fun", context="decision2")
def buissness_before_pleasure_peasant():
  print(f"you decide to ignore the riddle and keep having fun until you get awoken in the real world just to see that same clown in real life. he shouts your name {name}, you shall die for your ignorance. startled you get up and run. but he quickly responds and snaps your neck. is this a dream? im afraid not")

@when("follow the riddle",context="decision2")
def wise_choice_peasant():
  print(f"you deicde to think about what the clown said and all of a sudden the world around you starts to shift into a new reality where you can spawn anything you want but a warning in the sky shows a startling message {name} will die tomorrow by 5pm. to prevent this you must kill the clown. would you like to ignore the warning or fight the clown?")

@when("remove the clown", context="decision3")
def game_of_wills():
  set_context("final decision")
  print(f"you realize you can still control your dreams and you decide to will away the clown. the clown begins to fade away but as it fades it leaves a black void that begins consuming everything around it. you decide to wake up and you find out your house is on fire. your roomate screams your name. {name} THE HOUSE IS ON FIRE WE HAVE TO LEAVE. you get up still in a daze as smoke fills your lungs. there is a way out through your window but there is a 20 feet drop which will break some bones. you have 2 options sit and die or jump. ")

@when("wake up", context="decision3")
def death_by_blaze():
  print(f"you wake up and a fire has consumed your bed in flams and as it begins to consume your body you realize its hopeless and you turn to your side to die. as you look at the clock before your end you see the time. 5:00PM game over {name} your dead")

@when("jump", context="final decision")
def oof_your_hospital_biil():
  print(f"you jump and as you fall you hear your bones crunch under you. you can no longer walk but you survived {name} you are pulled into an ambulance and firefighters put out the flames in the house. what the firefighters said started the fire is the most unsettling thing to you. the accelerant... was paper and gasoline.. but not any paper it was confetti paper.. what clowns use. and whats more is there was a note left on your door and it reads the following. see you at the hospital {name} as you recieve these news the police start an investigation into the arson and they uncover other instances of this happening to other people and find links between the incidents... but your not worried about that. because in the corner of your room... he sees you ******end of game******")



@when("sit and burn", context="final decision")
def are_you_dumb():
  set_context("final decision")
  print(f"you realize its hopeless and you just sit there and die. {name} died in arson fire. 4/22/1999-5/6/21")





start()
