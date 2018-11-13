import matplotlib.pyplot as plt
import numpy as np
from numpy import arange,sin,pi
from matplotlib.patches import Circle

period=1
amp=1

def pos_to_radians(pos):
    return (pos/period) * 2 * pi

def radians_to_pos(radians):
    return (radians / (2 * pi)) * period

def draw_sine_pos(pos,radians):
    current_y = amp * sin(pos_to_radians(pos))
    current_cos = amp * np.cos(radians)
    plt.plot((-1*amp,current_cos-amp,pos ,pos),(0,current_y,current_y,0))

def draw_line_with_pos(pos):
    draw_sine_pos(pos,pos_to_radians(pos))

def draw_line_with_radians(radians):
    draw_sine_pos(radians_to_pos(radians),radians)

def draw_circle():
    patch= plt.Circle((-1*amp,0),fill=False, radius= amp)
    ax=plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')

def draw_sine():
    length = 4.0
    t = arange(0,length,0.01)
    plt.plot(t, sin(2/period*pi*t))
    plt.xticks(arange(4))

draw_circle()
draw_sine()

#Add a line
plt.plot((-2*amp,5),(0,0))

#Draw
draw_line_with_pos(0.125)
draw_line_with_pos(0.3)
draw_line_with_pos(1.6)
#draw_line_with_radians(1.8)

plt.show()
