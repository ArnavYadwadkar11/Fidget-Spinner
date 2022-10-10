from turtle import *

state = {"turn":0}

def spinner():
    clear()
    angle = state["turn"]/10
    right(angle)
    forward(100)
    dot(120,"red")
    back(100)
    right(120)
    forward(100)
    dot(120,"green")
    back(100)
    right(120)
    forward(100)
    dot(120,"blue")
    back(100)
    right(120)
    update()

def animate():
    if state["turn"]>0:
        state['turn'] = state["turn"]-1
    spinner()
    ontimer(animate,20)

def flick():
    state["turn"] = state["turn"] + 10
    
setup(width=400, height=400, startx=600, starty=100)
hideturtle()
tracer(False)
width(20)
onkey(flick, "space")
listen()
animate()
done()