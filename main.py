import random
import os
import time

# Woorden
words = ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier', 'fotografie', 'waardebepaling', 'specialiteit', 'verzekering', 'universiteit', 'heesterperk']
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6
guessed_letters = set()

# Afbeeldingen
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

# Het spel
print("Welcome bij Galgje!")

while attempts > 0 and '_' in guessed:
    os.system('clear')
    print(HANGMAN_PICS[6 - attempts])
    print("\nWord:", ' '.join(guessed))
    print(f"Guesses left: {attempts}")
    print("Guessed letters:", ', '.join(sorted(guessed_letters)))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Voeg astublieft een enkelvoudig alphabetische letter.")
        time.sleep(1)
        continue

    if guess in guessed_letters:
        print("Je hebt deze letter al geprobeert.")
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
        print("Fout!")
        time.sleep(1)

# Resultaat
os.system('clear')
print(HANGMAN_PICS[6 - attempts])
if '_' not in guessed:
    print("\nGefeliciteerd! Je hebt het woord geraden:", word)
else:
    print("\nGame Over! Het woord was:", word)