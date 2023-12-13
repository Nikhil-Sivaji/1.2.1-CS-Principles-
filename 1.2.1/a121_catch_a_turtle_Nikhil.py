# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trtl
import random as rand



#-----game configuration----

score = 0
size = 3# size of turtle
color = "green"# color of turtle
turtleshape = "turtle" # shape of turtle
speed = 3# spped of turtle
font_setup = ("Arial",20,"normal")
#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False



#-----initialize turtle----
 #catch a turtle turtle
turtle = trtl.Turtle()
turtle.shape(turtleshape)#adds  shape of turtle
turtle.speed(speed)# the speed is added to the turtle
turtle.shapesize(size)# adds size of turtle
turtle.fillcolor(color)# adds color of turtle
 #Score turtle
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-200,200)
score_writer.pendown()
score_writer.hideturtle()
#counter turtle
counter = trtl.Turtle()
counter.penup()
counter.goto(200,200)
counter.pendown()
counter.hideturtle()

#-----game functions--------

#turtle clicked function teleports the turtle after clicked
def turtleclicked(x,y):
        global timer_up
        if (not timer_up):
                  update_score()
                  changepos()

        else:
             turtle.hideturtle()
  
#Changes the position of the turtle
def changepos():
    newXpos = rand.randint(-200,200)
    newYpos = rand.randint(-150,150)
    turtle.penup()# hides the trail
    turtle.hideturtle()# hides the turtle
    turtle.goto(newXpos,newYpos)
    turtle.showturtle()# shoes in back again

def update_score():
      score_writer.clear()
      global score 
      score += 1
      score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


#-----events----------------

turtle.onclick(turtleclicked)




wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) # timer 
wn.mainloop()