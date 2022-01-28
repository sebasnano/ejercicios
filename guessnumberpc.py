import random


def guessnumberpc(x):
    print("welcome to game")
    print(f"Selec a number come in 1 y {x}")

    limitInf = 1
    limitSup = x

    answer = ""

    while answer != "c":
        if limitInf != limitSup:
            predict = random.randint(limitInf, limitSup)
        else:
            predict = limitInf

        answer = input(
            f"My answer is {predict}, Si es mayor (A), Si es menor (B), Si es correcta (C): "
        ).lower()

        if answer == "a":
            limitSup = predict - 1
        elif answer == "b":
            limitInf = predict + 1

    print("The Pc guessed")


guessnumberpc(int(input("Number max: ")))
