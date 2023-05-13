import random
import time

scores = 0
cmpScores = 0
print("this is a game of rock paper scissors. ")
time.sleep(1.5)
print("you can simply play one game or multiple by entering a number.")
time.sleep(2)
games = int(input("How many games do you want to play: "))
print("GAME ON!")
time.sleep(1)
for i in range(games):
  computer = random.randint(0,2)
  play = int(input("Enter 0 for rock , 1 for scissors, 2 for paper: "))
  if play == 0:
    print("You chose rock")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
  elif play == 1:
    print("You chose scissors")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
  else:
    print("You chose paper")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
  if computer == 0:
    print("Computer chose rock")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
  elif computer == 1:
    print("Computer chose scissors")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
  else:
    print("Computer chose paper")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
  if play == computer:
    print("DRAW!!")
    time.sleep(1.5)
    print(f"Scores:\nyou : {scores}\nComputer : {cmpScores}")
    time.sleep(1.5)
  elif play ==0 and computer == 1:
    print("YOU WIN!. ROCK CRUSHES SCISSORS")
    time.sleep(1.5)
    scores+=1
    print(f"Scores:\nyou : {scores}\nComputer : {cmpScores}")
    time.sleep(1.5)
  elif play == 1 and computer == 2:
    print("YOU WIN!. SCISSORS CUTS PAPER")
    time.sleep(1.5)
    scores+=1
    print(f"Scores:\nyou : {scores}\nComputer : {cmpScores}")
    time.sleep(1.5)
  elif play >=2 and computer == 0:
    print("YOU WIN!. PAPER WRAPS ROCK")
    time.sleep(1.5)
    scores+=1
    print(f"Scores:\nyou : {scores}\nComputer : {cmpScores}")
    time.sleep(1.5)
  elif play ==1 and computer == 0:
    print("COMPUTER WINS!. ROCK CRUSHES SCISSORS")
    time.sleep(1.5)
    cmpScores+=1
    print(f"Scores:\nyou : {scores}\nComputer : {cmpScores}")
    time.sleep(1.5)
  elif play == 2 and computer == 1:
    print("COMPUTER WINS!. SCISSORS CUTS PAPER")
    time.sleep(1.5)
    cmpScores+=1
    print(f"Scores:\nyou : {scores}\nComputer : {cmpScores}")
    time.sleep(1.5)
  elif play ==0 and computer == 2:
    print("COMPUTER WINS!. PAPER WRAPS ROCK")
    time.sleep(1.5)
    cmpScores+=1
    print(f"Scores:\nyou : {scores}\nComputer : {cmpScores}")
    time.sleep(1.5)
print(f"your score is {scores}, and the computer scored {cmpScores}")
time.sleep(1)
if scores > cmpScores:
  print("CONGRATULATIONS YOU WON THIS GAME.")
else:
  print("BETTER LUCK NEXT TIME. THE COMPUTER WON THIS ONE.")