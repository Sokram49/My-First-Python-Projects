''' Dumb Word Search I tried to make with ChatGPT '''

import random
import string

original_word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
word_list = list(original_word_list)
rows, cols = 12, 12

def random_letter():
    return random.choice(string.ascii_lowercase)

grid = [[random_letter() for _ in range(cols)] for _ in range(rows)]
discovered_words = {}

def place_word(word):
    row = random.randint(0, rows - 1)
    col = random.randint(0, cols - 1)
    direction = random.choice([(0, 1), (1, 0)])

    for letter in word:
        if 0 <= row < rows and 0 <= col < cols:
            grid[row][col] = letter
        else:
            return
        
        row += direction[0]
        col += direction[1]

def display_grid():
    for row in grid:
        print(" ".join(row))

while True:
    print("--- Word Search Puzzle ---")

    grid = [[random_letter() for _ in range(cols)] for _ in range(rows)]

    for word in word_list:
        place_word(word)

    display_grid()
    
    while word_list:
        guess = input("Enter a word you've found: ").lower()

        if guess in word_list:
            word_list.remove(guess)

        display_grid()

    print("Congratulations! You found all the words.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing Word Search Puzzle. Goodbye.")
        break
