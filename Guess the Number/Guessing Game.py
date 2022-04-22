from email import feedparser
from itertools import count
import random

'''
# Guess the Number (computer)
def user_guess(x):
    """Generates a random value between 1 and x"""
    computer_number = random.randint(1, x)
    player_guess = 0
    while player_guess != computer_number:
        player_guess = int(
            input(f"I thought of a number between 1 and {x}, try to guess:\n")
        )
        if player_guess > computer_number:
            print("Too high, try again! ")
        elif player_guess < computer_number:
            print("Too low, try again! ")

    print(f"Bullseye! You've guessed, the number was {computer_number}")
'''

# Guess the Number (user)


def comp_guess(x):
    start = 1
    end = x
    feedback = ""
    print(f"Think a Number betwee 1 and {x}, I'll try to guess it!\n")
    while feedback != "c" and start != end:
        computer_guess = random.randint(start, end)
        feedback = str(
            input(
                f"Is {computer_guess} too high (enter H);\n"
                "Too low (enter L).\n"
                "Or i've nailed it (enter C)\n"
            )
            .lower()
            .strip()
        )
        if feedback == "h":
            high_guess = computer_guess - 1

        elif feedback == "l":
            lower_guess = computer_guess + 1

    print("I'm such a nice boya!!!")


comp_guess(5)
