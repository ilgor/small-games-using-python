import turtle
import time
import random

delay = [0.08]
step = 5
body_parts = []

class Coor:
    x = step
    y = 0

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0) # Dont let it draw automatically

food = turtle.Turtle()
food.shape('square')
food.color('red')
food.shapesize(stretch_wid=0.5, stretch_len=0.5)
food.penup()
food.goto(-200, 100)

def create_body_part():
    new_body = turtle.Turtle()
    new_body.shape("square")
    new_body.color("white")
    new_body.shapesize(stretch_wid=0.5, stretch_len=0.5)
    new_body.penup()
    return new_body

snake_head = create_body_part()
snake_head.goto(-350, 0)

def turtle_up():
    Coor.x = 0
    Coor.y = step

def turtle_down():
    Coor.x = 0
    Coor.y = -step

def turtle_left():
    Coor.x = -step
    Coor.y = 0

def turtle_right():
    Coor.x = step
    Coor.y = 0

def check_for_food(x, y):
    if x == food.xcor() and y == food.ycor():
        new_body = create_body_part()
        body_parts.append(new_body)
        
        new_x = random.randint(-350, 350)
        x_remainder = new_x % step
        if x_remainder > 0:
            new_x = new_x - x_remainder

        new_y = random.randint(-250, 250)
        y_remainder = new_y % step
        if y_remainder > 0:
            new_y = new_y - y_remainder

        food.goto(new_x, new_y)
        delay[0] = delay[0] - 0.005
    
def check_baunderies(x, y):
    if x >= 400:
        x = -400
    elif x <= -400:
        x = 400
    elif y >= 300:
        y = -300
    elif y <= -300:
        y = 300
    return x, y

def move():
    current_head_position_x = snake_head.xcor()
    current_head_position_y = snake_head.ycor()

    check_for_food(current_head_position_x, current_head_position_y) 
    current_head_position_x, current_head_position_y = check_baunderies(current_head_position_x, current_head_position_y)   

    snake_head.goto(current_head_position_x + Coor.x, current_head_position_y + Coor.y)

    if len(body_parts) > 0:
        tail = body_parts.pop()
        tail.goto(current_head_position_x, current_head_position_y)
        body_parts.insert(0, tail)
        
screen.listen()
screen.onkey(turtle_up, 'Up')
screen.onkey(turtle_down, 'Down')
screen.onkey(turtle_left, 'Left')
screen.onkey(turtle_right, 'Right')


while True:
    screen.update()
    move()
    time.sleep(delay[0])