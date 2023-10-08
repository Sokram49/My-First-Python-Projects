''' Simple Hangman game with the help of ChatGPT '''

word = "random"
word_progress = ["_"] * len(word)
incorrect_guesses = 0
wrong_letters = []

def display_hangman(incorrect_guesses):
    head = "  O   |"
    body = "  |   |"
    left_arm = " /|   |"
    right_arm = " /|\  |"
    left_leg = " /    |"
    right_leg = " / \  |"
    
    hangman = ["  +---+",
               "  |   |",
               "      |",
               "      |",
               "      |",
               "========"]
    
    for i in range(incorrect_guesses):
        if i == 0:
            hangman[2] = head
        elif i == 1:
            hangman[3] = body
        elif i == 2:
            hangman[3] = left_arm
        elif i == 3:
            hangman[3] = right_arm
        elif i == 4:
            hangman[4] = left_leg
        elif i == 5:
            hangman[4] = right_leg
        
    for line in hangman:
        print(line)

def display_word_progress(word_progress):
    word_display = " ".join(word_progress)
    print(f"Word Progress: {word_display}")

def display_word_bank(wrong_letters):
    word_bank = ", ".join(wrong_letters)
    print(f"Wrong Letters: {word_bank}")

while True:
    display_hangman(incorrect_guesses)
    display_word_progress(word_progress)
    display_word_bank(wrong_letters)

    guess = input("Guess a letter: ").lower()

    if len(guess) > 1 or guess.isdigit():
        print("Invalid guess.")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_progress[i] = guess
    else:
        incorrect_guesses += 1
        wrong_letters.append(guess)

    if "".join(word_progress) == word:
        print(f"You guessed the word! which was: {word}")
        replay = input("Would you like to play again? (y/n): ").lower()
        if replay == "y":
            incorrect_guesses = 0
            wrong_letters = []
            continue
        else:
            print("Thank you for playing.")
            break

    elif incorrect_guesses >= 6:
        print(f"The word was: {word}. Better luck next time.")
        replay = input("Would you like to play again? (y/n): ").lower()
        if replay == "y":
            incorrect_guesses = 0
            wrong_letters = []
            continue
        else:
            print("Thank you for playing.")
            break
