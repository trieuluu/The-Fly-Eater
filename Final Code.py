# Jonathan Rogers and Trieu Luu
# Prototype of Final Project

from turtle import *
from random import randrange
import time
import datetime
import winsound

FRAMES_PER_SECOND = 10


def setWindow(title):
    # This function sets size, coordinates, color and title of window
    # Input a string title
    screen = Screen()                       # initiates screen
    screen.screensize(6000, 6000)            # screen size
    screen.bgcolor("#C70039")               # screen color
    screen.setworldcoordinates(-3000,-3000,3000,3000)# screen coordinates
    screen.title(title)                     # screen title

def getCurrentTime():
    # This function gets CurrentTime in format: hh:mm:ss
    # returns a string in format: hh:mm:ss
    return datetime.datetime.time(datetime.datetime.now())

def countingTime(strStartTime, strEndTime):
    # This function calculates how much time passed
    # Inputs: two strings (hh:mm:ss) of start time
    # Return: a float indicates how much time has passed (in seconds)

    # convert inputs to string
    strStartTime = str(strStartTime)
    #print(strStartTime)    # testing

    strEndTime = str(strEndTime)
    #print(strEndTime)      # testing
    
    startList = strStartTime.split(':')
    endList = strEndTime.split(':')

    #print(startList)       # testing
    #print(endList)         # testing
    
    # convert to float
    for i in range(len(startList)):
        startList[i] = float(startList[i])

    for i in range(len(endList)):
        endList[i] = float(endList[i])
        
    # convert total time in seconds
    startTime = (startList[0] * 3600) + (startList[1] * 60) + (startList[2])
    endTime = (endList[0] * 3600) + (endList[1] * 60) + (endList[2])

    # calculate how much time has passed
    timePass = endTime - startTime

    return timePass
    
def soundEffect(soundfile):
    # This function plays sound effects
    # Input: name of the sound file (.wav)
    # Download free sound effects: https://www.audiomicro.com/free-sound-effects
    
    winsound.PlaySound(soundfile, winsound.SND_FILENAME)    

def turnRight():
    global turtleUser

    turtleUser.right(15)

    
def turnLeft():
    global turtleUser

    turtleUser.left(15)


    
def move():
    global turtleUser
    global moving

    try:
        if moving:
            turtleUser.penup()
            turtleUser.forward(100)    
    except NameError:
        print("Keep moving!")
    
def start():
    global moving

    moving = True
    move()


def stop():
    global moving

    moving = False
    

def jumpToCenter(turtle):
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.pendown()

    
def obsMove(turtle):
    turtle.forward(250)
    ontimer(move, 1000 // 1000000)

def obstacle(turtle, number):
    global turtleUser
    global i
    global flaglist
    
    
    #print(turtle)
    if (flaglist[number] == 0):              # when the flag is not set, obstacle turtle is not eaten
        turtle.penup()
        turtle.speed(75)

        turtle.right(randrange(-100, 100))
        obsMove(turtle)
        turtle.left(randrange(-100, 100))
        obsMove(turtle)

        if ((4000 > abs(turtle.xcor()) > 3000) or (4000 > abs(turtle.ycor()) > 3000)):
            jumpToCenter(turtle)

        if (abs(turtleUser.xcor()) > 3000) or (abs(turtleUser.ycor()) > 3000):
            jumpToCenter(turtleUser)

        if (((turtle.xcor() - turtleUser.xcor())**2 + (turtle.ycor() - turtleUser.ycor())**2) < 1000000):
            turtle.color("blue")
            i = i + 1
            print(i)
            flaglist[number] = 1
            print("fly",number, "is eaten.")
            turtle.hideturtle()
       
        
    
def main():
    
    setWindow("Eat the Flies!!!!!")
    global turtleUser
    global i
    global moving
    global flaglist                 

    flaglist = [0] * 16            # creates flag list
    
    
    i = 0                            # counting flies eaten
  
    
    turtleUser = Turtle()
    turtleUser.shape("turtle")
    turtleUser.color("#1B2631")
    turtleUser.resizemode("user")
    turtleUser.penup()
    turtleUser.setpos(-2500, -2500)
    
    
    obs1 = Turtle()
    obs2 = Turtle()
    obs3 = Turtle()
    obs4 = Turtle()
    obs5 = Turtle()
    obs6 = Turtle()
    obs7 = Turtle()
    obs8 = Turtle()
    obs9 = Turtle()
    obs10 = Turtle()
    obs11 = Turtle()
    obs12 = Turtle()
    obs13 = Turtle()
    obs14 = Turtle()
    obs15 = Turtle()

    timestart = getCurrentTime()
    print(timestart)
    
    onkey(turnRight, "Right")
    onkey(turnLeft, "Left")
    onkey(start, "Up")
    onkey(stop, "Down")
    listen()
   
   
    while(i <= 14):
        
        obstacle(obs1, 1)
        obstacle(obs2, 2)
        obstacle(obs3, 3)
        obstacle(obs4, 4)
        obstacle(obs5, 5)
        obstacle(obs6, 6)
        obstacle(obs7, 7)
        obstacle(obs8, 8)
        obstacle(obs9, 9)
        obstacle(obs10, 10)
        obstacle(obs11, 11)
        obstacle(obs12, 12)
        obstacle(obs13, 13)
        obstacle(obs14, 14)
        obstacle(obs15, 15)

    screen = Screen()
    screen.clearscreen() 
    
    timeend = getCurrentTime()
    print(timeend)

    duration = countingTime(timestart, timeend)
    print(duration)

    screen.bgcolor("green")
        
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.color("yellow")
    
    text.write("Congratulations!  ", False, align = "center", font = ("Arial", 12, "normal"))

    text.goto(0, -500)

    soundEffect("sound1.wav")
    
    text.write("You finished in {0} seconds!".format(int(duration)), False, align = "center", font = ("Arial", 12, "normal"))

    text.goto(0, -1000)

    text.write("Click to exit", False, align = "center", font = ("Arial", 12, "normal"))

    screen.exitonclick()
        
if __name__ == "__main__":
    main()

