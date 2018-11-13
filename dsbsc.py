import numpy as np 
import matplotlib.pyplot as plt

seconds_to_plot = 1.0 #TODO scale with fl_lf
plot_precision = 10000.0

u_lf=0.5
f_hf=100
f_lf=2

#Adding some info within table
plt.title("DSBSC - Modulating single tone of " 
          + str(u_lf) + " V and " + str(f_lf) + " Hz" 
          + " over carrier of " + str(f_hf) + " Hz")

# Setting up axes
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.ylabel("voltage (u)")
plt.xlabel("time (s)")
time_axis = np.arange(0.0, seconds_to_plot, seconds_to_plot / plot_precision)

#Basic signals
base_signal    = u_lf * np.sin(2 * np.pi * f_lf * time_axis)
carrier_signal =        np.sin(2 * np.pi * f_hf * time_axis) 
dsbsc_signal   = base_signal * carrier_signal 

#Plotting dsb-sc-signal and indicating base-singnal against
plt.plot(time_axis,  dsbsc_signal, color="blue", label="dsbsc")
plt.plot(time_axis,  base_signal,  color="red",  label="single tone +")
plt.plot(time_axis, -base_signal,  color="grey", label="single tone -")

plt.legend()
plt.margins(0.05)

plt.show()
