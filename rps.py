import random


def game():
    user = input("Enter your options (r = rock, p = paper, s = scissors).\n").lower()
    pc = random.choice(["r", "p", "s"])

    if user == pc:
        return "Draw"

    if winner(user, pc):
        return "Winner"

    return "Game Over"


def winner(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "p" and opponent == "r")
        or (player == "s" and opponent == "p")
    ):
        return True
    else:
        return False


print(game())