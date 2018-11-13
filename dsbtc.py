import numpy as np 
import matplotlib.pyplot as plt

seconds_to_plot = 1.0
plot_precision = 10000.0

def plot_line(h,color="red"):
    plt.plot([0, seconds_to_plot], [h, h], lw=1, linestyle='--', color=color)

u_lf=0.5
u_hf=1
f_hf=50
f_lf=2


plt.title("DSBSC - Modulating single tone of " + str(f_lf) + "V and " 
          + str(f_lf) + " Hz" 
          + " over carrier of " + str(f_hf) + " Hz (M = " 
          + str(int(u_lf/u_hf * 100))  + "%)")


plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.ylabel("voltage (u)")
plt.xlabel("time (s)")

time_axis = np.arange(0.0, seconds_to_plot, seconds_to_plot / plot_precision)

# Calculations
base_signal =    u_lf * np.sin(2 * np.pi * f_lf *  time_axis)
carrier_signal = u_hf * np.sin(2 * np.pi * f_hf * time_axis)
am_signal = carrier_signal * (u_hf + base_signal)

#Plotting am
plt.plot( time_axis, am_signal,color="blue",label="am" )

#Plotting envelop
plt.plot( time_axis, base_signal + u_hf,color="red",label="single tone +",linestyle="--")
plot_line(u_hf,color="red")
plot_line(u_hf - u_lf,color="red")
plot_line(u_hf + u_lf,color="red")

#Plotting "reverse" envelop
plt.plot( time_axis, -(base_signal + u_hf),color="grey",label="single tone -",linestyle="--")
plot_line(-(u_hf),color="grey")
plot_line(-(u_hf - u_lf),color="grey")
plot_line(-(u_hf + u_lf),color="grey")

plt.legend()
plt.margins(0.05)

plt.show()