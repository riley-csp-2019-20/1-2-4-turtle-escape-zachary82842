# Import turtle as trtl
import turtle as trtl
import random

# Name a varibale
mz = trtl.Turtle()
mz.speed(0)
mz.pensize(3)
mz.hideturtle()

# Make a new turtle
mt = trtl.Turtle()
mt.shape("turtle")
mt.color("green")
mt.turtlesize(.75)
mt.goto(0,-7)

side = 200
wall_width = 8
door_width = 22

def drawDoor():
    mz.penup()
    mz.forward(door_width)
    mz.pendown()

def drawBarrier():
    mz.right(90)
    mz.forward(wall_width*2)
    mz.backward(wall_width*2)
    mz.left(90)

def mt_up():
    mt.setheading(90)
    mt.forward(10)

def mt_down():
    mt.setheading(270)
    mt.forward(10)

def mt_right():
    mt.setheading(0)
    mt.forward(10)

def mt_left():
    mt.setheading(180)
    mt.forward(10)

for i in range(25):

    if i < 17:
        door = random.randint(door_width, side - door_width*2)
        barrier = random.randint(wall_width*2, side - door_width*2)
        if door < barrier:

            mz.forward(door)

            drawDoor()

            mz.forward(barrier - door - door_width)
            #barrier
            drawBarrier()


            mz.forward(side - barrier)


        else:
            mz.forward(barrier)

            drawBarrier()

            mz.forward(door - barrier)

            drawDoor()

            #forward rest of the way
            mz.forward(side - door_width - door)

    mz.right(90)
    side = side - wall_width






wn = trtl.Screen()
wn.onkeypress(mt_up, "Up")
wn.onkeypress(mt_down, "Down")
wn.onkeypress(mt_right, "Right")
wn.onkeypress(mt_left, "Left")
wn.listen()
wn.mainloop()
