from adventurelib import *
#name=str(input("enter your name: ")
def restart():
  print("Welcome to the school pop quiz! type in 'begin' to begin, and type in 'hint' when you need a hint on a certain question. There are four questions. Good luck!")

print(restart())

def incorrect():
  print("That is incorrect! type in 'restart' to retake the quiz")

answers= ["6.022x10^23", "q2", "q3", "q4"]
hints= ["What are the amount of atoms in a mole?", "q2h", "q3h", "q4h"]

@when("restart")
def restart():
  print("Welcome to the school pop quiz! type in 'begin' to begin, and type in 'hint' when you need a hint on a certain question. There are four questions. Good luck!")
@when("begin")
def q1():
  print("What is the numerical factor of Avogadro's number?")
  answer1=input()
  if answer1 == answers[0]:
    print("That is correct!")
  else:
    print("That is incorrect! type in 'restart' to retake the quiz.")



start()