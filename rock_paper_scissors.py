"""
Rock, Paper, Scissors game inspired by Tech With Tim's second project in the 5 Mini Python Projects video.
Draw feature added where the program displays how many draws occurred.
"""

import random

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
  user_pick = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
  if user_pick == "q":
    break

  if user_pick not in options:
    continue

  random_number = random.randint(0, 2)
  # rock: 0, paper: 1, scissors: 2
  computer_pick = options[random_number]
  print("Computer picked", computer_pick)

  if user_pick == "rock" and computer_pick == "scissors":
    print("You won!")
    user_wins += 1
    continue

  elif user_pick == "paper" and computer_pick == "rock":
    print("You won!")
    user_wins += 1

  elif user_pick == "scissors" and computer_pick == "paper":
    print("You won!")
    user_wins += 1

  elif user_pick == computer_pick:
    print("It's a draw")
    draws += 1

  else:
    print("You lost")
    computer_wins += 1

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Draws:",draws)
print("Bye Bye")
