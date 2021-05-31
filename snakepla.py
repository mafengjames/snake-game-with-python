import turtle
import time
import random

# creating screen
screen = turtle.Screen()
screen.title("hungry viper")
screen.setup(width=1000, height=1000)
screen.bgcolor("cyan")
screen.tracer(0)

#creating the snake head
head = turtle.Turtle()
head.penup()
head.shape("circle")
head.color("green")
head.goto(0,0)
head.direction = "stop"
head.speed(0)

#  snake food
food = turtle.Turtle()
food.penup()
food.color("red")
food.shape("circle")
x = random.randint(-400, 400)
y = random.randint(-400, 400)
food.goto(x,y)
food.direction = "stop"
# function
def sama():
    head.direction = "up"
def kasa():
    head.direction = "down"
def dama():
    head.direction = "right"
def ahgu():
    head.direction = "left"

def tafi():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)

# creating the body
snake =[]

# binding key
screen.listen()
screen.onkey(sama, "Up")
screen.onkey(kasa, "Down")
screen.onkey(dama, "Right")
screen.onkey(ahgu, "Left")


#main game loop
while True:
    screen.update()
    # checking for colllision
    tafi()
    time.sleep(0.1)
    if head.distance(food) < 20:
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        food.goto(x,y)

new_segment = turtle.Turtle()
new_segment.penup()
new_segment.shape("square")
new_segment.color(green)
new_segment.speed(0)

snake.append(new_segment)
#moving segment to reverse




screen.mainloop()