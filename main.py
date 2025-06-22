import random
import os
import time

#woorden#
words =  ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier', 'fotografie', 'waardebepaling', 'specialiteit', 'verzekering', 'universiteit', 'heesterperk']
word = random.choice(words)
guessed =['_'] * len(word)
attempts = 5
geraden_letters = set()

#afbeeldingen#
Galgje_Pics = [
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

#het spel#
print ("Welkom bij Galgje!")

while attempts > 0 and '_' in guessed:
  os.system ('clear')
print(Galgje_Pics[5-attempts])
print("\nWord",''.join("geraden"))
print(f"pogingen over: {attempts}")
print("geraden letters:", ', '.join(sorted(geraden_letters)))

guess = input("Raad een letter: ").lower()

if not guess.isalpha() or len(guess) != 1:
  print("Ongeldige invoer. Probeer opnieuw.")
  time.sleep(1)
  continue
if guess in geraden_letters:
  print("Je hebt deze letter al geraden. Probeer opnieuw.")
  time.sleep(1)
  continue
  
geraden_letters.add(guess)
if guess in word:
  for i,c in enumerate(word):
    if c==guess:
       guessed[i]=guess
    print("Goed geraden!")
    time.sleep(1)
    
#resultaat#
os.system('clear')
print(Galgje_Pics[5-attempts])
if '_' not in guessed:
  print("\nGefeliciteerd! Je hebt het woord geraden:", word)
else:
  print("\nHelaas, je hebt het woord niet geraden. Het woord was:",word)