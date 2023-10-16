# This file was created by: Daniel Csubak

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
have t
'''

# import package...
import turtle
import random
from turtle import *
# The os module allows us to access the current directory in order to access assets...
import os
import winsound
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
from random import randint

# setup the game folders using the os module...
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
sounds_folder = os.path.join(game_folder, 'sounds')

# Used this resource to include sound...
# https://www.youtube.com/watch?v=w6g8PO-Pqp4
def play_rock():
    winsound.PlaySound(os.path.join(sounds_folder, 'rock.wav'), winsound.SND_ASYNC)
def play_paper():
    winsound.PlaySound(os.path.join(sounds_folder, 'paper.wav'), winsound.SND_ASYNC)
def play_scissors():
    winsound.PlaySound(os.path.join(sounds_folder, 'scissors.wav'), winsound.SND_ASYNC)

# setup the width and height for the window...
WIDTH, HEIGHT = 1000, 400
rock_w, rock_h = 256, 280
paper_w, paper_h = 256, 204
scissors_w, scissors_h = 256, 170
player_choice = ""
cpu_choice = ""

# setup the Screen class using the turtle module...
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar...
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")

# canvas object...
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates...
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image...
rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
cpu_rock_instance = turtle.Turtle()
# setup the paper image using the os mudule as rock_image... 
paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
cpu_paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image...
scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
cpu_scissors_instance = turtle.Turtle()

# Defining the rock image and where it is relitevaly to everything else...
def show_rock(x,y):
    # add the rock image as a shape...
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance...
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved...
    rock_instance.penup()
    # set the position of the rock_instance...
    rock_instance.setpos(x,y)

def cpu_show_rock(x,y):
    screen.addshape(cpu_rock_image)
    cpu_rock_instance.shape(cpu_rock_image)
    cpu_rock_instance.penup()
    cpu_rock_instance.setpos(x,y)

# Defining the paper image and where it is relitevaly to everything else...
def show_paper(x,y):
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    screen.addshape(cpu_paper_image)
    cpu_paper_instance.shape(cpu_paper_image)
    cpu_paper_instance.penup()
    cpu_paper_instance.setpos(x,y)
# Defining the paper image and where it is relitevaly to everything else...
def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

def cpu_show_scissors(x,y):
    screen.addshape(cpu_scissors_image)
    cpu_scissors_instance.shape(cpu_scissors_image)
    cpu_scissors_instance.penup()
    cpu_scissors_instance.setpos(x,y)

text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

show_rock(-300,0)
show_paper(0,0)
show_scissors(300,0)

# when game results in tie...
def tie ():
    text.clear()
    text.penup()
    text.setpos(0,150)
    text.write("It's a tie.", False, "left", ("Arial", 24, "normal"))
# when game results in player winning...
def player_win ():
    text.clear()
    text.penup()
    text.setpos(0,150)
    text.write("Player wins.", False, "left", ("Arial", 24, "normal"))
#when game results in cpu winning...
def cpu_win ():
    text.clear()
    text.penup()
    text.setpos(0,150)
    text.write("Computer wins.", False, "left", ("Arial", 24, "normal"))

# function that passes through wn onlick
def mouse_pos(x, y):
    cpu_picked = cpu_select()
    player_picked = ''
    if collide(x,y,rock_instance,rock_w,rock_h):
        text.clear()
        text.write("Player picked Rock.", False, "left", ("Arial", 24, "normal"))
        paper_instance.hideturtle()
        scissors_instance.hideturtle()
        user_choice = "rock" 
    elif collide(x,y,paper_instance,paper_w,paper_h):
        text.clear()
        text.write("Player picked Paper.", False, "left", ("Arial", 24, "normal"))
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        paper_instance.backward(300)
        user_choice = "paper"
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        text.clear()
        text.write("Player picked Scissors.", False, "left", ("Arial", 24, "normal"))
        rock_instance.hideturtle()
        paper_instance.hideturtle()
        scissors_instance.backward(550)
        user_choice = "scissors"
    else:
        return print("Please Pick One...")

    possible_choices = ["rock", "paper", "scissors"]
    cpu_choice = random.choice(possible_choices)

    if cpu_choice == "rock":
        cpu_rock_instance.shape(rock_image)
        cpu_rock_instance.penup()
        cpu_rock_instance.setpos(300,0)
        if user_choice == "paper":
            text.outcome.write("Player Wins.", False, "Center", ("Arial", 24, "normal"))
        elif user_choice == "scissors":
            text.outcome.write("Player Loses", False, "Center", ("Arial", 24, "normal"))
        else:
            text.outcome.write("Tie!!!", False, "Center", ("Arial", 24, "normal"))
    elif cpu_choice == "paper":
        cpu_paper_instance.shape(paper_image)
        cpu_paper_instance.penup()
        cpu_paper_instance.setpos(300,0)
        if user_choice == "scissors":
            text.outcome.write("Player Wins.", False, "Center", ("Arial", 24, "normal"))
        elif user_choice == "rock":
            text.outcome.write("Player Loses", False, "Center", ("Arial", 24, "normal"))
        else:
            text.outcome.write("It's a Tie.", False, "Center", ("Arial", 24, "normal"))

    else:
        cpu_choice == "scissors"
        cpu_scissors_instance.shape(scissors_image)
        cpu_scissors_instance.penup()
        cpu_scissors_instance.setpos(300,0)
        if user_choice == "rock":
            text.outcome.write("You Win!!!", False, "Center", ("Arial", 24, "normal"))
        elif user_choice == "paper":
            text.outcome.write("You Lose!!!", False, "Center", ("Arial", 24, "normal"))
        else:
         text.outcome.write("Tie!!!", False, "Center", ("Arial", 24, "normal"))


screen.onclick (mouse_pos)
text.penup()
text.setpos(-100,150)
text.write("Please choose Rock, Paper or Scissors.", False, "left", ("Arial", 24, "normal"))
text.setpos(72,320)
screen.mainloop()
