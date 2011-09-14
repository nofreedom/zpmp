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

samples = np.arange(0, number_sample_per_chip)
baseband_wave = np.sin(samples*fc/(2*pi))
plt.figure()
plt.plot(samples,baseband_wave)
plt.show()
