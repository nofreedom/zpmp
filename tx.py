#!/usr/bin/python
import math
import numpy as np
import matplotlib.pyplot as plt
from common import *


def baseband_wave(x_axis):
    half_sine_wave = np.sin(x_axis*pi/number_sample_per_chip)
    return half_sine_wave

def dsss_modulate(data):
    r = []
    for j in range(2):
        if j:
            tmp = (data & 0xf0) /16
        else:
            tmp = data & 0xf
        for i in range(32):
            if chip[tmp][i]:
                r.append(baseband_wave(x_axis))
            else:
                r.append((-1)*baseband_wave(x_axis))

    return np.concatenate(r)

def compose_frame(data):    #input data is a sequence of byte
    r = []
    r.append(dsss_modulate(0))
    r.append(dsss_modulate(0))
    r.append(dsss_modulate(0))
    r.append(dsss_modulate(0)) #4 successive 0, the preamble
    r.append(dsss_modulate(0xa7)) #start of frame
    r.extend([dsss_modulate(i) for i in data])
    return np.concatenate(r)

def tx(data):
    return compose_frame(data)

#plt.plot(x_axis,baseband_wave(x_axis))

#x_axis = range(0,16)
#r = np.zeros((16,16))
#for i in range(0,16):
#    for j in range(0,16):
#        r[i][j] = np.correlate(chip[i], chip[j])
#    print "%r\n"%r[i]

#r = dsss_modulate(0)
#plt.figure()
#plt.plot(range(len(r)), r, linestyle='dashed', marker='o')
#plt.show()




