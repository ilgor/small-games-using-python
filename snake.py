import turtle
import time


class Coor:
    step = 10
    x, y = step, 0

delay = 0.1
bodies = []

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black") 
screen.setup(width=800, height=600, startx=None, starty=None)
turtle.screensize(canvwidth=800, canvheight=600)
screen.tracer(0) # stop auto draw


def create_new_body():
    body = turtle.Turtle()
    body.shape("square")
    body.color("white")
    body.shapesize(stretch_wid=0.5, stretch_len=0.5)
    body.penup()
    body.speed(0) # the fastest
    return body

snake_head = create_new_body()
snake_head.goto(-300, 0)
screen_x, screen_y = screen.screensize()

def snake_up():
    Coor.x = 0
    Coor.y = Coor.step

def snake_down():
    Coor.x = 0
    Coor.y = - Coor.step

def snake_left():
    Coor.x = - Coor.step
    Coor.y = 0

def snake_right():
    Coor.x = Coor.step
    Coor.y = 0

def snake_add_body():
    new_body = create_new_body()
    bodies.append(new_body)

def move():
    snake_x = snake_head.xcor()
    snake_y = snake_head.ycor()
    if snake_x > screen_x / 2:
        snake_x = -screen_x / 2
    elif snake_x < -screen_x / 2:
        snake_x = screen_x / 2
    elif snake_y > screen_y / 2:
        snake_y = -screen_y / 2
    elif snake_y < -screen_y / 2:
        snake_y = screen_y / 2

    snake_head.goto(snake_x + Coor.x, snake_y + Coor.y)
    
    if len(bodies) > 0:
        tail = bodies.pop()
        tail.goto(snake_x, snake_y)
        bodies.insert(0, tail)

    
screen.listen()
screen.onkey(snake_up, "Up")
screen.onkey(snake_down, "Down")
screen.onkey(snake_left, "Left")
screen.onkey(snake_right, "Right")
screen.onkey(snake_add_body, "b")

while True:
    screen.update()
    move()
    time.sleep(delay)

