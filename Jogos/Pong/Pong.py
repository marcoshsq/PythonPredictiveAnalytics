# Script:
# 1. importing the relevant Libraries (Turtle, Pygame.);
# 2. Create the game screen;
# 3. Create the paddles , their positions, shapes and colors;
# 4. Movement function, and Player commands;
# 5. Create the ball, add collision;
# Note: collision goes inside the main game loop.
# 6. Finally, details, score, texts & etc.

import turtle
import winsound


# Game screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_01 = 0
score_02 = 0

# racket 01 (left racket)
racket_01 = turtle.Turtle()
racket_01.speed(0)
racket_01.shape("square")
racket_01.color("white")
racket_01.shapesize(stretch_wid=5, stretch_len=1)
racket_01.penup()
racket_01.goto(-350, 0)


# racket 02 (right racket)
racket_02 = turtle.Turtle()
racket_02.speed(0)
racket_02.shape("square")
racket_02.color("white")
racket_02.shapesize(stretch_wid=5, stretch_len=1)
racket_02.penup()
racket_02.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# This are gonna make the ball move by a number of pixel
ball.dx = 0.3
ball.dy = 0.3


# Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 01: 0 | Player 02: 0", align="center", font=("Courier", 24, "normal"))


# Game Functions
def racket_01_up():
    """Add 20px to the left racket,
    to make it go up
    """
    y = racket_01.ycor()
    y += 40
    racket_01.sety(y)


def racket_01_down():
    """Add 20px to the left racket,
    to make it go down
    """
    y = racket_01.ycor()
    y -= 40
    racket_01.sety(y)


def racket_02_up():
    """Add 20px to the right racket,
    to make it go up
    """
    y = racket_02.ycor()
    y += 40
    racket_02.sety(y)


def racket_02_down():
    """Add 20px to the right racket,
    to make it go down
    """
    y = racket_02.ycor()
    y -= 40
    racket_02.sety(y)


# Keyboard binding
# For the left racket
wn.listen()
wn.onkeypress(racket_01_up, "w")
wn.listen()
wn.onkeypress(racket_01_down, "s")
# For the left racket
wn.listen()
wn.onkeypress(racket_02_up, "Up")
wn.listen()
wn.onkeypress(racket_02_down, "Down")

# Main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Game Borders
    # Here, is if the ball touches the border it value will reverse

    # Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Down border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_01 += 1
        pen.clear()
        pen.write(
            f"Player 01: {score_01} | Player 02: {score_02}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_02 += 1
        pen.clear()
        pen.write(
            f"Player 01: {score_01} | Player 02: {score_02}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    # Racket collision

    # Right racket
    if (
        ball.xcor() > 340
        and ball.xcor() < 350
        and (ball.ycor() < racket_02.ycor() + 40)
        and (ball.ycor() > racket_02.ycor() - 40)
    ):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Right racket
    if (
        ball.xcor() < -340
        and ball.xcor() > -350
        and (ball.ycor() < racket_01.ycor() + 40)
        and (ball.ycor() > racket_01.ycor() - 40)
    ):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
