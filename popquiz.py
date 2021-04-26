from adventurelib import *
#name=str(input("enter your name: ")
def restart():
  print("Welcome to the school pop quiz! type in 'begin' to begin, and type in 'hint' when you need a hint on a certain question. There are four questions. Good luck!")

print(restart())

answers= ["6.022x10^23", "4", "q3", "q4"]
hint= ["What are the amount of atoms in a mole?", "Use addition", "q3h", "q4h"]
current_q=0

@when("restart")
def restart():
  print("Welcome to the school pop quiz! type in 'begin' to begin, and type in 'hint' when you need a hint on a certain question. There are four questions. Good luck!")

@when("begin")
def q1():
  print("What is the numerical factor of Avogadro's number?")
  set_context("question")

@when("hint", context= "question")
def give_hint():
  global current_q
  print(hint[current_q])

@when("ANSWER", context= "question")
def give_ans1(answer):
  global current_q
  if answer == answers[current_q]:
    print("That is correct! Type 'question two' to go to the second question")
    current_q + 1
    set_context("answered")
  else:
    print("That is incorrect! type in 'restart' to retake the quiz.")
@when("question two")
def q2():
  print("what is 2+2?")
  set_context("question")

@when("ANSWER", context="question")
def give_ans2(answer):
  global current_q
  if answer == answers[current_q]:
    print("That is correct! Type 'q3' to go to the third question")
    current_q + 1
    set_context("answered")





