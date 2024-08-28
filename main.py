from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()


def bind_events():
    screen.onkey(screen.bye, "q")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


bind_events()

while game_is_on:
    snake.move()
    screen.update()
    if snake.head.distance(food) < 15:
        food.move()
        snake.extend_snake()
        scoreboard.update()
    if snake.collided_with_wall() or snake.collided_with_self():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
