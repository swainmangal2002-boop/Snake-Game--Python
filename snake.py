"""Snake, classic arcade game with Restart and Quit"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
game_over = False

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def reset_game():
    """Restart the game."""
    global snake, aim, food, game_over
    clear()
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    food = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
    game_over = False
    move()

def quit_game():
    """Quit the game."""
    bye()

def move():
    """Move snake forward one segment."""
    global game_over

    if game_over:
        return

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'blue')
        update()
        game_over = True
        print("Game Over! Press R to Restart or Q to Quit")
        return

    snake.append(head)

    if head == food:
        print('Snake length:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 80)  # speed control (lower = faster)

# ---- Setup ----
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Movement keys
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Restart & Quit keys
onkey(reset_game, 'r')
onkey(reset_game, 'R')
onkey(quit_game, 'q')
onkey(quit_game, 'Q')

move()
done()
