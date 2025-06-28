# Import required library
import turtle

# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
sc.tracer(0) # Turn off screen updates

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)


# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(0) # Set speed to 0 for consistent movement
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 0.1 # Smaller step for smoother movement
hit_ball.dy = -0.1 # Smaller step for smoother movement

# Score
left_player = 0
right_player = 0

# Display score
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Left_player : 0 Right_player : 0", align="center", font=("Courier", 24, "normal"))


# Functions to move paddles
def left_pad_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

def left_pad_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

def right_pad_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)

def right_pad_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)

# Keyboard bindings
sc.listen()
sc.onkeypress(left_pad_up, "w")
sc.onkeypress(left_pad_down, "s")
sc.onkeypress(right_pad_up, "Up")
sc.onkeypress(right_pad_down, "Down")


# Game loop
while True:
    sc.update()

    # Move the ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Border checking
    if hit_ball.ycor() > 290:
        hit_ball.sety(290)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -290:
        hit_ball.sety(-290)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 490:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        score.clear()
        score.write("Left_player : {} Right_player : {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -490:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        score.clear()
        score.write("Left_player : {} Right_player : {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-360)
        hit_ball.dx *= -1