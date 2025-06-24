#imports#
import random
import os
import time

#woorden#
words = [
    'informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier',
    'fotografie', 'waardebepaling', 'specialiteit', 'verzekering',
    'universiteit', 'heesterperk'
]

#variabelen#
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6
geraden_letters = set()
game_aan = True

#afbeeldingen#
Galgje_Pics = [
    """
          +---+
          |   |
              |
              |
              |
              |
         =========""", """
          +---+
          |   |
          O   |
              |
              |
              |
         =========""", """
          +---+
          |   |
          O   |
          |   |
              |
              |
         =========""", """
          +---+
          |   |
          O   |
         /|   |
              |
              |
         =========""", """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
         =========""", """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
         =========""", """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
         ========="""
]

#functie van het spel#
def galgje_loop():
     global attempts
     os.system('clear')
     print(Galgje_Pics[6 - attempts])
     print("\nWord", ' '.join(guessed))
     print(f"Pogingen over: {attempts}")
     print("Geraden letters:", ', '.join(sorted(geraden_letters)))

     guess = input("Raad een letter: ").lower()

     if not guess.isalpha() or len(guess) != 1:
          if attempts == 1:
               print("Je hebt geen pogingen meer over!")
          else:
               print("Ongeldige invoer. Probeer opnieuw.")
          time.sleep(1)
          attempts -= 1
          return

     if guess in geraden_letters:
          print("Je hebt deze letter al geraden. Probeer opnieuw.")
          time.sleep(1)
          attempts -= 1
          return

     geraden_letters.add(guess)

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
     return


print("Welkom bij Galgje!")

#game loop#
while game_aan:
     while attempts > 0 and '_' in guessed:
          galgje_loop()

     #resultaat#
     geldig_antwoord = False
     while not geldig_antwoord:
          os.system('clear')
          print(Galgje_Pics[6 - attempts])
          if '_' not in guessed:
               print("\nGefeliciteerd! Je hebt het woord geraden:", word)
          else:
               print(
                   "\nHelaas, je hebt het woord niet geraden. Het woord was:",
                   word)

          print("\nWil je nog een keer spelen? (ja/nee)")
          antwoord = input("> ").lower()
          if antwoord == "nee":
               geldig_antwoord = True
               game_aan = False
               print("\nBedankt voor het spelen!")
               time.sleep(1)
          elif antwoord == "ja":
               geldig_antwoord = True
               word = random.choice(words)
               guessed = ['_'] * len(word)
               attempts = 6
               geraden_letters = set()
               os.system('clear')
          else:
               print("Ongeldige invoer, probeer opnieuw.")
               time.sleep(1)
