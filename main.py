import random
import os
import time

# Words list with random selection
words = ['python', 'hangman', 'sebas', 'nina', 'coding']
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6
guessed_letters = set()

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

print("Welcome to Hangman!")

while attempts > 0 and '_' in guessed:
    os.system('clear')
    print(HANGMAN_PICS[6 - attempts])
    print("\nWord:", ' '.join(guessed))
    print(f"Guesses left: {attempts}")
    print("Guessed letters:", ', '.join(sorted(guessed_letters)))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        sleep(1)
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        time.sleep(1)
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i, c in enumerate(word):
            if c == guess:
                guessed[i] = guess
        print("Correct!")
        time.sleep(1)
    else:
        attempts -= 1
        print("Wrong!")
        time.sleep(1)

# Results
os.system('clear')
print(HANGMAN_PICS[6 - attempts])
if '_' not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)