from tkinter import *
from PIL import Image, ImageTk
from random import randint

from pyparsing import col

# Main Window.
game_window = Tk()
# Window name.
game_window.title("Rock, Paper & Scissors")
# BG collor.
game_window.configure(background="#5533cc")

# Icons
paper_left = ImageTk.PhotoImage(Image.open("paper_left.png"))
paper_right = ImageTk.PhotoImage(Image.open("paper_right.png"))

rock_left = ImageTk.PhotoImage(Image.open("rock_left.png"))
rock_right = ImageTk.PhotoImage(Image.open("rock_right.png"))

scissors_left = ImageTk.PhotoImage(Image.open("scissors_left.png"))
scissors_right = ImageTk.PhotoImage(Image.open("scissors_right.png"))

# Inserting the icons.
player_label = Label(game_window, image=scissors_left.png, bg="#5533cc")
python_label = Label(game_window, image=scissors_right.png, bg="#5533cc")
player_label.grid(row=1, column=0)
python_label.grid(row=1, column=4)

# Score.
player_score = Label(game_window, text=0, font=100, bg="#9b59b6", fg="white")
python_score = Label(game_window, text=0, font=100, bg="#9b59b6", fg="white")
player_score.grid(row=1, column=1)
python_score.grid(row=1, column=3)

# indicators
player_indicator = Label(game_window, font=50, text="Player", bg="#9b59b6", fg="white")
python_indicator = Label(game_window, font=50, text="Python", bg="#9b59b6", fg="white")
player_indicator.grid(row=0, column=3)
python_indicator.grid(row=0, column=1)

# messages
msg = Label(game_window, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)


def updateMessage(x):
    msg["text"] = x


# update user score
def player_score():
    """Update the player score."""
    score = int(player_score["text"])
    score += 1
    player_score["text"] = str(score)


# update computer score
def computer_score():
    """Update the computer score."""
    score = int(computer_score["text"])
    score += 1
    computer_score["text"] = str(score)


# check winner
def result_msg(player, computer):
    if player == computer:
        result_msg("Its a tie!!!")

    elif player == "rock":
        if computer == "paper":
            result_msg("You loose")
            computer_score()

        else:
            result_msg("You Win")
            player_score()

    elif player == "paper":
        if computer == "scissor":
            result_msg("You loose")
            computer_score()

        else:
            result_msg("You Win")
            player_score()

    elif player == "scissor":
        if computer == "rock":
            result_msg("You loose")
            computer_score()

        else:
            result_msg("You Win")
            player_score()

    else:
        pass


# update choices
choices = ["rock", "paper", "scissor"]


def update_choice(x):
    """Update the icon on the screen"""

    # For the computer
    comp_choice = choices[randint(0, 2)]
    if comp_choice == "rock":
        python_label.configure(image=rock_right)

    elif comp_choice == "paper":
        python_label.configure(image=paper_right)

    else:
        python_label.configure(image=scissors_right)

    # For the Player
    if x == "rock":
        player_label.configure(image=rock_left)

    elif x == "paper":
        player_label.configure(image=paper_left)

    else:
        player_label.configure(image=scissors_left)

    result_msg(x, comp_choice)


# buttons
rock = Button(
    game_window,
    width=20,
    height=2,
    text="ROCK",
    bg="#FF3E4D",
    fg="white",
    command=lambda: update_choice("rock"),
).grid(row=2, column=1)

paper = Button(
    game_window,
    width=20,
    height=2,
    text="PAPER",
    bg="#FAD02E",
    fg="white",
    command=lambda: update_choice("paper"),
).grid(row=2, column=2)

scissor = Button(
    game_window,
    width=20,
    height=2,
    text="SCISSOR",
    bg="#0ABDE3",
    fg="white",
    command=lambda: update_choice("scissor"),
).grid(row=2, column=3)


# Main Loop.
game_window.mainloop()

# Greatness awaits (づ｡◕‿‿◕｡)づ:
