''' Game inspired by Tech With Tim's first project in his 3 Mini Python Projects - For Beginners video
    I figured out how to add a draw feature so if two end up with the same score it shows that '''

import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll

while True:
    players = input("Enter number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_index in range(players):
        print(f"\nIt's player {player_index + 1}'s turn now!")
        print(f"You start your turn with a score of: {player_scores[player_index]}\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1...")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}!")

            print(f"Your score is: {current_score}")

        player_scores[player_index] += current_score
        print(f"\nYou end your turn with a score of: {player_scores[player_index]}")

max_score = max(player_scores)
for score in player_scores:
    winner = player_scores.index(max_score)
    winner_two = player_scores.index(score)
    if score != max_score:
        print(f"Player {winner + 1} is the winner with a score of: {max_score}")
        break
    else:
        print(f"It's a draw between player {winner + 1} and player {winner_two + 1} with a score of {max_score}")
