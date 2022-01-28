import random
import string

from words import words
from visuallives import visuallives


def wordValidator(words):
    word = random.choice(words)

    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hanged():
    print("Welcome to Game!")

    word = wordValidator(words)

    letterGuess = set(word)
    letterGuessed = set()
    alphabet = set(string.ascii_uppercase)

    lives = 7

    while len(letterGuess) > 0 and lives > 0:
        print(
            f"Te quedan {lives} vidas y has usado estas letras: {' '.join(letterGuessed)}"
        )

        wordReading = [letter if letter in letterGuessed else "-" for letter in word]

        print(visuallives[lives])
        print(f"Palabra: {' '.join(wordReading)}")
        
        letterUser = input("Escoja una letra: ").upper()
        
        if letterUser in alphabet - letterGuessed:
            letterGuessed.add(letterUser)
            
            if letterUser in letterGuess:
                letterGuess.remove(letterUser)
                print('')
            else:
                lives -= 1
                print(f"la letra {letterUser} no esta")
        elif letterUser in letterGuessed:
            print(f"la letra {letterUser} ya la escojiste")
        else:
            print(f"la letra {letterUser} no es valida")
    if lives == 0:
        print(f"{visuallives[lives]}")
        print(f"Perdiste, la palabra era {word}")
    else:
        print(f"Acertaste, la palabra era {word}")
        
        
hanged()