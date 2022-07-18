from turtle import *
from random import randrange
from random import randint
from random import choice
import time

#pantalla
wn=Screen()
wn.title("Tetris")
wn.bgcolor("Black")
wn.setup(750,950)
wn.tracer(0)

addshape("Bloque amarillo_1 gif.gif")
addshape("Bloque azul_1 gif.gif")
addshape("Bloque cyan_1 gif.gif")
addshape("Bloque lima_1 gif.gif")
addshape("Bloque morado_1 gif.gif")
addshape("Bloque naranja_1 gif.gif")
addshape("Bloque rojo_1 gif.gif")
#Con esto se podria cambiar la forma de los bloques para que se vea mas estetico 
def color_forma(col):
    if col=="#FF0000":
        return "Bloque rojo_1 gif.gif"
    if col=="#FFD700":
        return "Bloque amarillo_1 gif.gif"
    if col=="#FFA500":
        return "Bloque naranja_1 gif.gif"
    if col=="#0000FF":
        return "Bloque azul_1 gif.gif"
    if col=="#00FFFF":
        return "Bloque cyan_1 gif.gif"
    if col=="#C71585":
        return "Bloque morado_1 gif.gif"
    if col=="#00FF00":
        return "Bloque lima_1 gif.gif"
#Juego 
class Tetris:
    def __init__(self):
        self.shape="square"
        self.size=[2.5,2.5,1]
        self.bloq=None
        self.bloques=[]
        self.direccion="stop"
        self.puntaje=0
    def palo(self):
        color=choice(colores)
        ver_hor=randint(1,2)
        palo=[]
        x_r=randrange(-300,300,50)
        for NumBloq in range(3):
            if ver_hor==1:
                x=NumBloq*50 + x_r
                y=0 + 500
            if ver_hor==2:
                x=0 + x_r
                y=NumBloq*50 + 500
            bloque= Turtle()
            bloque.penup()
            bloque.shape(color_forma(color))
            bloque.goto(x,y)
            palo.append(bloque)
        self.bloq=palo
        self.bloques.append(palo)

    def ele(self):
        color=choice(colores)
        ele=[]        
        ver_hor=choice(["horizontal","vertical"])
        lado=choice(["izquierda","derecha"])
        arriba=choice(["arriba","abajo"])
        x_r=randrange(-300,300,50)
        for NumBloq in range(4):
            if ver_hor=="horizontal":
                x=NumBloq*50 +x_r
                y=0 + 500
            if ver_hor=="vertical":
                x=0 + x_r
                y=NumBloq*50 + 500
            bloque=Turtle()
            bloque.penup()
            bloque.shape(color_forma(color))
            if NumBloq<3:
                bloque.goto(x,y)
            if NumBloq==3:
                if ver_hor=="horizontal":
                    if lado=="izquierda":
                        if arriba=="arriba":
                            bloque.goto(x-50,y+50)
                        if arriba=="abajo":
                            bloque.goto(x-150,y+50)
                    if lado=="derecha":
                        if arriba=="arriba":
                            bloque.goto(x-50,y-50)
                        if arriba=="abajo":
                            bloque.goto(x-150,y-50)
                if ver_hor=="vertical":
                    if lado=="izquierda":
                        if arriba=="arriba":
                            bloque.goto(x-50,y-50)
                        if arriba=="abajo":
                            bloque.goto(x-50,y-150)
                    if lado=="derecha":
                        if arriba=="arriba":
                            bloque.goto(x+50,y-50)
                        if arriba=="abajo":
                            bloque.goto(x+50,y-150)
            ele.append(bloque)
        self.bloq=ele
        self.bloques.append(ele)

    def cuadrado(self):
        color=choice(colores)
        cuadrado=[]
        x_r=randrange(-300,300,50)
        for NumBloq in range(2):
            x=NumBloq*50 + x_r
            y=0 + 500
            bloque=Turtle()
            bloque.penup()
            bloque.shape(color_forma(color))
            bloque.goto(x,y)
            cuadrado.append(bloque)
        for NumBloq in range(2):
            x=NumBloq*50 + x_r
            y=0 + 550
            bloque=Turtle()
            bloque.penup()
            bloque.shape(color_forma(color))
            bloque.goto(x,y)
            cuadrado.append(bloque)
        self.bloq=cuadrado
        self.bloques.append(cuadrado)

    def te(self):
        color=choice(colores)
        te=[]
        x_r=randrange(-300,300,50)
        ver_hor=choice(["horizontal","vertical"])
        arr_aba=choice(["arriba","abajo"])
        for NumBloq in range(4):   
            if ver_hor=="horizontal":
                if arr_aba=="arriba":
                    if NumBloq==3:
                        x=x_r+50
                        y=550
                    else:
                        x=NumBloq*50 + x_r
                        y=500
                if arr_aba=="abajo":
                    if NumBloq==3:
                        x=x_r+50
                        y=450
                    else:
                        x=NumBloq*50 + x_r
                        y=500
            if ver_hor=="vertical":
                if arr_aba=="arriba":
                    if NumBloq==3:
                        x=x_r+50
                        y=550
                    else:
                        x=x_r
                        y=NumBloq*50 + 500
                if arr_aba=="abajo":
                    if NumBloq==3:
                        x=x_r -50
                        y= 550
                    else: 
                        x=x_r
                        y=NumBloq*50 +500                    
            bloque=Turtle()
            bloque.penup()
            bloque.shape(color_forma(color))
            bloque.goto(x,y)
            te.append(bloque)
        self.bloq=te
        self.bloques.append(te)

    def zeta(self):
        color=choice(colores)
        zeta=[]
        ver_hor=choice(["horizontal","vertical"])
        arr_aba=choice(["arriba","abajo"])
        x_r=randrange(-300,300,50)
        for NumBloq in range(4):            
            if ver_hor=="horizontal":
                if arr_aba=="arriba":
                    if NumBloq<2:
                        x=NumBloq*50+x_r
                        y=500
                    if NumBloq>=2:
                        x=(NumBloq-1)*50+x_r
                        y=550
                if arr_aba=="abajo":
                    if NumBloq<2:
                        x=NumBloq*50 + x_r
                        y=550
                    if NumBloq>=2:
                        x=(NumBloq-1)*50 + x_r
                        y=500
            if ver_hor=="vertical":
                if arr_aba=="arriba":
                    if NumBloq<2:
                        x=x_r
                        y=NumBloq*50 + 500
                    if NumBloq>=2:
                        x=x_r +50
                        y=(NumBloq-1)*50 +500
                if arr_aba=="abajo":
                    if NumBloq<2:
                        x=x_r
                        y=NumBloq*50 +500
                    if NumBloq>=2:
                        x=x_r-50
                        y=(NumBloq-1)*50 + 500
            bloque=Turtle()
            bloque.penup()
            bloque.shape(color_forma(color))
            bloque.goto(x,y)
            zeta.append(bloque)
        self.bloq=zeta
        self.bloques.append(zeta)
                
#Funciones
def izquierda():
    juego.direccion="left"
def derecha():
    juego.direccion="right"
def abajo():
    juego.direccion="down"

def jugabilidad():
    mov=0
    if juego.direccion=="stop":
        mov=0
    if juego.direccion=="left":
        if mov_izq==True:
            mov=-50
    if juego.direccion=="right":
        if mov_der==True:
            mov=50
    if juego.direccion=="down":
        if mov_aba==True:
            mov=-50
    for i in range(len(juego.bloq)):
        if juego.direccion=="down":
            y=juego.bloq[i].ycor()
            juego.bloq[i].sety(y+mov)
        else:
            x=juego.bloq[i].xcor()
            juego.bloq[i].setx(x+mov)
    juego.direccion="stop"


#teclado
wn.listen()
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")
wn.onkeypress(abajo,"Down")
          #rojo   #gold   #orange #blue   #cyan #violetred #Lime
colores= "#FF0000 #FFD700 #FFA500 #0000FF #00FFFF #C71585 #00FF00".split()
mov_izq=True
mov_der=True
mov_aba=True
juego=Tetris()
primer_bloque=choice([juego.palo,juego.ele,juego.te,juego.zeta,juego.cuadrado])
primer_bloque()
bloques=[]
colision=False
perdida=False

#puntaje
punt=Turtle()
punt.penup()
punt.color("white")
punt.ht()
punt.goto(0,425)
punt.write(f"Puntaje: {juego.puntaje}", align="Center",font=("Courirer",24,"normal"))
punt.speed(0)


#ciclo
while True:
    if perdida==True:
        game_over=Turtle()
        game_over.penup()
        game_over.ht()
        game_over.color("white")
        game_over.write("Game Over",align="center",font=("Courier",40,"normal"))
        game_over.goto(0,0)
        time.sleep(5)
        break
    if perdida==False:
        wn.update()

    if colision==True:
        for i in range(len(juego.bloq)):
            if juego.bloq[i].ycor()==450:
                perdida=True
    time.sleep(0.2)
    punt.clear()
    punt.write(f"Puntaje: {juego.puntaje}", align="Center",font=("Courirer",24,"normal"))
#  [juego.palo,juego.ele,juego.te,juego.zeta,juego.cuadrado]

    if colision==True:
        bloque_aleatorio=choice([juego.palo,juego.ele,juego.te,juego.zeta,juego.cuadrado])
        bloque_aleatorio()
        colision=False
    if colision==False:
        bajo=[]
        for i in range(len(juego.bloq)):
            bajo.append(juego.bloq[i].ycor())
        min_bajo=bajo.index(min(bajo))      
        for i in range(len(juego.bloq)): 
            y=juego.bloq[i].ycor()
            juego.bloq[i].sety(y-50)
            for j in range(len(juego.bloques)):
                for k in range(len(juego.bloques[j])):
                    if juego.bloq[i].xcor()==350:
                        mov_der=False
                    if juego.bloq[i].xcor()==-350:
                        mov_izq=False
                    if juego.bloq[i].ycor()==-350:
                        mov_aba=False
                    if j < len(juego.bloques)-1:
                        if juego.bloq[i].ycor()==juego.bloques[j][k].ycor()+50 and juego.bloq[i].xcor()==juego.bloques[j][k].xcor():
                            colision=True
                        #evita que se mueva en ciertas condiciones
                        if juego.bloq[i].ycor()==-400 or juego.bloq[i].ycor()==-350 or juego.bloq[i].ycor()==-300:
                            mov_aba=False
                        if juego.bloq[i].ycor()==juego.bloques[j][k].ycor() and juego.bloq[i].xcor()==juego.bloques[j][k].xcor()-50:
                            mov_der=False 
                        if juego.bloq[i].ycor()==juego.bloques[j][k].ycor() and juego.bloq[i].xcor()==juego.bloques[j][k].xcor()+50:
                            mov_izq=False
                        if juego.bloq[i].ycor()==juego.bloques[j][k].ycor()+100 and juego.bloq[i].xcor()==juego.bloques[j][k].xcor():
                            mov_aba=False
                        if juego.bloq[i].ycor()==juego.bloques[j][k].ycor()+50 and juego.bloq[i].xcor()==juego.bloques[j][k].xcor():
                            mov_aba=False
                            mov_der=False
                            mov_izq=False                        
        if juego.bloq[min_bajo].ycor()<=-450:
            colision=True
    #debajo de jugabilidad tiene que ir esos mov_... para que funcionen correctamente
    jugabilidad()
    mov_der=True
    mov_izq=True
    mov_aba=True
    
    #Lineas
    columnas=[-450,-400,-350,-300,-250,-200,-150,-100,-50,0,50,100,150,200,250,300,350,400,450]
    filas=[-350,-300,-250,-200,-150,-100,-50,0,50,100,150,200,250,300,350]
    for columna in columnas:
        linea=0
        indice1=[]
        indice2=[]
        for fila in filas:
            for i in range(len(juego.bloques)):
                for j in range(len(juego.bloques[i])):
                    if juego.bloques[i][j].xcor()==fila and juego.bloques[i][j].ycor()==columna:
                        linea+=1
                        indice1.append(i)
                        indice2.append(j)
        if linea>=15:
            for k in range(len(indice1)):
                juego.bloques[indice1[k]][indice2[k]].goto(364733494,4324434)
            for i in range(len(juego.bloques)):
                for j in range(len(juego.bloques[i])):
                    if juego.bloques[i][j].ycor() >=columna:
                        y=juego.bloques[i][j].ycor()
                        juego.bloques[i][j].sety(y-50)
            juego.puntaje+=100
