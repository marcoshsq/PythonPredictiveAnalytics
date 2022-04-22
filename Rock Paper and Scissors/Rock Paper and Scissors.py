import random
import time

# I'll define some messages that'll repeat
def win():
    """Shows a victory message."""
    print("You won!!")


def lost():
    """Shows a defeat message."""
    print("You lost!!")


def tie():
    """Shows a tie message."""
    print("it's a tie")


def draw_line():
    """Makes and prints a kind of header."""
    print("-=" * 20)


# These three lines are python's logic
itens = ["Rock", "Paper", "Scissors"]
pc_choice = random.choice(itens)

# Game
player_count = 0
pc_count = 0
flag = True
while flag:
    # Game
    draw_line()
    print("Let's play JOKENPO")
    draw_line()
    player_choice = (
        str(input("What's your move: \nRock\nPaper\nScissors:\n")).lower().strip()
    )

    # This is just to add some drama
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO")
    time.sleep(1)

    # The player and the Python choice
    print(f"Python chose {pc_choice}")
    print(f"You chose {player_choice}")

    # Now we create the scenarios
    if (
        (player_choice == "rock" and pc_choice == "Rock")
        or (player_choice == "paper" and pc_choice == "Paper")
        or (player_choice == "scissors" and pc_choice == "Scissors")
    ):
        tie()
        ask = str(input("Let's play another? \n")).lower().strip()
        if ask == "yes":
            continue
        else:
            break

    elif (
        (player_choice == "rock" and pc_choice == "Scissors")
        or (player_choice == "paper" and pc_choice == "Rock")
        or (player_choice == "scissors" and pc_choice == "Paper")
    ):
        win()
        player_count += 1
        ask = str(input("Let's play another? \n")).lower().strip()
        if ask == "yes":
            continue
        else:
            break

    elif (
        (player_choice == "rock" and pc_choice == "Paper")
        or (player_choice == "paper" and pc_choice == "Scissors")
        or (player_choice == "scissors" and pc_choice == "Rock")
    ):
        lost()
        pc_count += 1
        ask = str(input("Let's play another? \n")).lower().strip()
        if ask == "yes":
            continue
        else:
            break

draw_line()
print(f"Results: Player {player_count} points | Python {pc_count} points")
draw_line()
