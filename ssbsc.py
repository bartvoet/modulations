import numpy as np 
import matplotlib.pyplot as plt

plt.title("SSBSC")

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.ylabel("voltage (u)")
plt.xlabel("time (s)")

seconds_to_plot = 1.0
plot_precision = 10000.0
time_axis = np.arange(0.0, seconds_to_plot, seconds_to_plot / plot_precision)

u_lf=0.5
f_hf=100
f_lf=2

base_signal = u_lf * np.sin(2 * np.pi * f_lf *  time_axis)
dsbsc_signal = u_lf * np.sin(2 * np.pi * f_hf * time_axis) * np.sin(2 * np.pi * f_lf *  time_axis)

plt.plot( time_axis, base_signal,color="red",label="single tone...")
plt.plot( time_axis, dsbsc_signal,color="blue",label="dsbsc" )
plt.plot( time_axis, -base_signal,color="grey")

plt.legend()
plt.margins(0.05)

plt.show()