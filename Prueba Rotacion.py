from turtle import * 
from time import sleep
addshape("Bloque amarillo_1 gif.gif")


class Util:
    def __init__(self):
        self.temp=0

util=Util()
wn=Screen()
wn.title("Prueba Rotacion")
wn.bgcolor("black")
wn.setup(width=750,height=950)
wn.tracer(0)

bloques=[]
for i in range(4):
    if i ==3:
        bloq=Turtle()
        bloq.penup()
        bloq.shape("Bloque amarillo_1 gif.gif")
        bloq.goto(50,(i*50)-50)
        bloques.append(bloq)
    else:
        bloq=Turtle()
        bloq.penup()
        bloq.shape("Bloque amarillo_1 gif.gif")
        bloq.goto(0,i*50)
        bloques.append(bloq)


def rot_izq():
    if util.temp==1:
        for i in range(len(bloques)):
            x=bloques[i].xcor()
            y=bloques[i].ycor()
            bloques[i].setx(-y)
            bloques[i].sety(-x)
        util.temp-=1
    elif util.temp==0:
        for i in range(len(bloques)):
            x=bloques[i].xcor()
            y=bloques[i].ycor()
            bloques[i].setx(y)
            bloques[i].sety(x)
        util.temp+=1


def rot_der():
    if util.temp==1:
        for i in range(len(bloques)):
            x=bloques[i].xcor()
            y=bloques[i].ycor()
            bloques[i].setx(y)
            bloques[i].sety(x)
        util.temp-=1 
    elif util.temp==0:
        for i in range(len(bloques)):
            x=bloques[i].xcor()
            y=bloques[i].ycor()
            bloques[i].setx(-y)
            bloques[i].sety(-x)
        util.temp+=1

wn.listen()
wn.onkeypress(rot_izq,"e")
wn.onkeypress(rot_der,"q")
while True:
    wn.update()
    sleep(0.05)
