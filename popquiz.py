from adventurelib import *
#name=str(input("enter your name: ")
def restart():
  print("Welcome to the school pop quiz! type in 'begin' to begin, and type in 'hint' when you need a hint on a certain question. There are four questions. Good luck!")

print(restart())
questions= ["q1","q2","q3","q4"]
answers= ["6.022x10^23", "4", "a3", "a4"]
hint= ["What are the amount of atoms in a mole?", "Use addition", "q3h", "q4h"]
current_q=0

@when("restart")
def restart():
  print("Welcome to the school pop quiz! type in 'begin' to begin, and type in 'hint' when you need a hint on a certain question. There are four questions. Good luck!")

@when("begin")
def q1():
  print(questions[current_q])
  set_context("question")

@when("hint", context= "question")
def give_hint():
  global current_q
  print(hint[current_q])

@when("ANSWER", context= "question")
def give_ans1(answer):
  global current_q
  if answer == answers[current_q]:
    print("That is correct! Type 'next question' to go to the next question")
    current_q = current_q+1
    set_context("answered")
  else:
    print("That is incorrect! type in 'restart' to retake the quiz.")
@when("next question")
def q2():
  print(questions[current_q])
  set_context("question")






