from ast import While
import random


def guessnumber(x):
    print("welcome to the game!")
    print("guess the number")

    randomNumber = random.randint(1, x)

    prediction = 0

    while prediction != randomNumber:
        prediction = int(input(f"guess a number come in 1 and {x}: "))
        
        if prediction < randomNumber:
            print("the number is less")
        elif prediction > randomNumber:
            print("the number is higher")
            
    print("Congratulation¡ you guessed the correct number {randomNumber}")


guessnumber(int(input("waht is the pc limit: ")))