# Generates multiple varying colored circles shifted up
import turtle as t
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_circle(size):
    t.pencolor(next(colors))
    t.circle(size)
    draw_circle(size + 5)

t.bgcolor('black')
t.speed('fast')
t.pensize(4)
draw_circle(40)
