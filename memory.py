"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# Letras que representan cada pareja (16 parejas, una letra por pareja)
LETTERS = 'ABCDEFGHIJKLMNOP'
tiles = list(range(16)) * 2 # Valores de las fichas: 16 números, cada uno repetido dos veces (32 fichas)
hide = [True] * 32 # True = ficha oculta, False = ficha destapada (una por cada ficha)
# mark: índice de la primera ficha destapada en este turno (None si no hay)
# taps: número de clics que ha hecho el jugador
state = {'mark': None, 'taps': 0}

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

def finished():
    # Devuelve True cuando todos los cuadros están destapados.
    # Si la lista hide ya no tiene ningún True, el juego terminó.
    return not any(hide)

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    state['taps'] += 1
    print('Taps:', state['taps'])  # Imprime el contador de taps en la consola

    spot = index(x, y)
        # Si el clic cayó fuera del tablero, no hace nada

    if spot >=len(hide):
        return

    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(32):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
   
   # Muestra la letra de la ficha marcada, si todavía está oculta
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 5)
        color('black')
        write(LETTERS[tiles[mark]], font=('Arial', 30, 'bold'), align='center')

#Dibuja el numero de taps
    up()
    goto(-200, 180)
    color('black')
    write(f"Taps: {state['taps']}", font=('Arial', 15, 'normal'))
       
  # Muestra un mensaje cuando todos los cuadros están destapados

    if finished():
        up()
        goto(0, -190)
        color('black')
        write('¡Completed in ' + str(state['taps']) + ' taps!',
              align='center', font=('Arial', 16, 'normal'))
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
