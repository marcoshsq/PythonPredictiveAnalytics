from tkinter import *
from PIL import Image, ImageTk

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

# Main Loop.
game_window.mainloop()
