'''
1. Random appearance of the shape on different parts of the screen
2. The event of a shape being clicked
3. The score updating
4. The timer updating
'''
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
xMin = 0
xMax = 112
yMin = 0
yMax = 324
score = 0
timer = 30
timerup = False
counterinterval = 1000
fontsetup = ("Arial", 20, "normal")
color = "blue"
shape = "circle"

#-----initialize turtle-----
t = trtl.Turtle()
t.shape(shape)
t.fillcolor(color)
t.penup()
t.hideturtle()

gamestart = trtl.Turtle()
gamestart.penup()
gamestart.goto(50, 0)
gamestart.write("Press to begin!", font=fontsetup)

scorewriter = trtl.Turtle()
scorewriter.penup()
scorewriter.goto(300, -300)
scorewriter.hideturtle()

counter = trtl.Turtle()
counter.penup()
counter.goto(-300, -300)
counter.hideturtle()

#-----game functions--------
def spot_clicked(x, y):
  t.goto(rand.randint(xMin, xMax), rand.randint(yMin, yMax))
  scorechange()
  addcolor()
  size()

def addcolor():
  colorlist = ["Red", "Yellow", "Purple", "Black", "Pink", "Blue", "Orange"]
  t.fillcolor(rand.choice(colorlist))
  t.stamp()
  t.fillcolor(color)

def size():
  sizechange = [5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, .5]
  t.turtlesize(rand.choice(sizechange))

def scorechange():
  global score
  score += 1
  scorewriter.clear()
  scorewriter.write(score, font=fontsetup)

def start_game(x, y):
  t.showturtle()
  countdown()
  gamestart.clear()

def countdown():
  global timer, timerUp
  counter.clear()
  if timer <= 0:
      timer -= 1
      counter.write("Time Is Up!", font=fontsetup)
      timerUp = True
  else:
      counter.write("timer: " + str(timer), font=fontsetup)
      timer -= 1
      counter.getscreen().ontimer(countdown, counterinterval)
#-----events----------------
gamestart.onclick(start_game)
t.onclick(spot_clicked)
wn = trtl.Screen()
wn.bgcolor("green")
wn.mainloop()