import random

color_picks = input("Enter colors to guess from: ")

color_list = color_picks.split()

random_color = random.choice(color_list)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess == random_color:
        print("You got it!")
        break
    else:
        print("Try again")

print("You got it in", guesses, "guesses")
