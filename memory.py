#a01651150
"""
1. Contar y desplegar el numero de taps
2. Detectar cuando todos los cuadros se han destapado
3. Central el dígito en el cuadro
4. Como un condimento de innovación al juego, Podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria ?
"""

from random import *
from turtle import *
from emoji import emojize

from freegames import path

car = path('car.gif')
# Se cambian los numeros por emojis para ayudar a la memoria
emojis2=[u'\U0001F34C', u'\U0001F34D',]
emojis=[u'\U0001F347', u'\U0001F348', u'\U0001F349', u'\U0001F34A', u'\U0001F34B', u'\U0001F34C', u'\U0001F34D', u'\U0001F34E', u'\U0001F34F', u'\U0001F350', u'\U0001F351',
        u'\U0001F352', u'\U0001F353', u'\U0001F95D', u'\U0001F345', u'\U0001F965',u'\U0001F347', u'\U0001F348', u'\U0001F349', u'\U0001F34A', u'\U0001F34B', u'\U0001F34C', 
        u'\U0001F34D', u'\U0001F34E', u'\U0001F34F', u'\U0001F350', u'\U0001F351', u'\U0001F352', u'\U0001F353', u'\U0001F95D', u'\U0001F345', u'\U0001F965']
tiles = list(emojis2) * 32
state = {'mark': None}
hide = [True] * 64
#Contador de taps y encontrados(1,2)
taps=0
founds = 0 

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps
    global founds 
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    #Se aumenta en 1 el contador de taps
    taps +=1

    #Se cuenta el nuemro de encontrados
    founds=0
    for a in hide:
        if a == False:
          founds += 1

   

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Se alinea texto al centro(3)
        goto(x + 25, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')

    #Se determina el ganador
    if founds==4:
        up()
        goto(0, 0)
        color('green')
        write('YOU WIN!!', font=('Arial', 30, 'normal'), align='center')

    #Contador de taps display(1)
    goto(-230,160)
    color("black")
    write(taps, font=('Arial', 30, 'normal'), align='center')
    
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(540, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()