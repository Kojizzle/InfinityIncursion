from adventurelib import *
#name=str(input("enter your name: ")
set_context("question")
def restart():
  print("Welcome to the school pop quiz! type in 'begin' to begin, and type in 'hint' when you need a hint on a certain question. There are four questions. Good luck!")

print(restart())
questions= ["Of the following, which cannot be causes of insomnia?","Of the following, which are symptoms of insomnia?","Which of gthe following is associated with the REM stage of sleep?"]
answers= ["another sleep wake disorder", "Difficulty sleeping one or more times per week", "rapid low voltage EEG", "High-amplitude brain waves"]
hint= ["Insonima is a sleep-wake disorder.", "Insomina is defined as a recurring difficulty sleeping.", "REM sleep is a dreaming stage, but requires less energy than others."]
current_q=0

@when("restart", context= "question")
def restart():
  print("Welcome to the school pop quiz! type in 'begin' to start, and type in 'hint' when you need a hint on a certain question. There are four questions. Good luck!")

@when("begin", context = "question")
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








