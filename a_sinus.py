import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
from numpy import arange,sin,pi
from matplotlib.patches import Circle

period=pi
amp=0.25
period=2 * amp * pi

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
    ax.set_yticklabels([])    
    ax.set_xticklabels([])
    plt.axis('scaled')

def draw_circle_p(p):
    patch= plt.Circle((p*amp,0),fill=False, radius= amp)
    ax=plt.gca()
    ax.add_patch(patch)
    ax.set_yticklabels([])    
    ax.set_xticklabels([])
    plt.axis('scaled')

def draw_sine(phase):
    length = 4.0
    t = arange(0,length,0.01)
    plt.plot(t, amp * sin(2/period*pi*t + phase))
    plt.xticks(arange(4))

def draw_sinel(phase,l,length):
    #length = 6.0
    t = arange(0,l,0.01)
    plt.plot(t, amp * sin(2/period*pi*t + phase))
    draw_line_with_pos(l)
    plt.xticks(arange(length + 1))


FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Een sinus...', artist='Matplotlib', comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
fig = plt.figure()


with writer.saving(fig, "writer_test.mp4", 100):
    frames = 500
    tl = 5.0  
    for i in range(frames):
        pos = tl * (float(i)  / float(frames))
        pi_times_radians = round(((pos/period) * 2) % 2,2)
        degrees = pi_times_radians * 180
        plt.gcf().clear()
        plt.title("(" + str(pi_times_radians) + ") * pi radians" + str(degrees) + " degrees" )
        draw_circle()
        draw_sinel(0, tl * (float(i)  / float(frames)),tl)
        plt.plot(  [-1*amp, tl], [0, 0] )
        writer.grab_frame()
