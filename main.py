from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Create the game Screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
# Turn animation off
screen.tracer(0)

# Create the paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Listen to keyboard
screen.listen()

# Move Right Paddle
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

# Move Left Paddle
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

# Create the ball
ball = Ball()

game_is_on = True

while game_is_on:

    # Add delay so the ball moves slower
    time.sleep(0.1)

    # Refresh the screen to show elements after turning animation off
    screen.update()

    # Move the ball
    ball.move()

    # Detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ycor()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_xcor()

# Keep the window open
screen.exitonclick()
