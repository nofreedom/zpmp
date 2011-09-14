#!/usr/bin/python
import math
import numpy as np
import matplotlib.pyplot as plt

fcarrier = 2400000000 #2.4GHz carrier
fs  = 32000000  #Sample rate at   32MHz
tc  = 1.0/2000000   #chip length in seconds
fc  = 1.0/(2*tc)    #the frequency of half-sine wave of chip
pi  = math.pi
number_sample_per_chip = fs/2000000 
x_axis = np.arange(0, number_sample_per_chip)

def baseband_wave(x_axis):
    half_sine_wave = np.sin(x_axis*2*pi/number_sample_per_chip)
    return half_sine_wave

plt.figure()
plt.plot(x_axis,baseband_wave(x_axis))
plt.show()
