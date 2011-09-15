#!/usr/bin/python
import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from common import *

def dem_engine(data, chip_index):
    index = 0
    sum = []
    while(index < len(data)):
        for j in range(32):
            tmp = 0
            for i in range(number_sample_per_chip):
                if index >= len(data): break
                tmp += data[index]
                index += 1
                print index
            sum.append(tmp)
            index += number_sample_per_chip
    r = np.correlate(chip[chip_index], sum)
    print r
    plt.plot(range(len(r)), r, 'b--', range(len(data)), data, 'r.')
    plt.show()
    os._exit(1)
    return r

def sync_det(data):
    p = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
    index = 0
    while(index < len(data)):
        for i in range(number_sample_per_chip):
            p[i].append(dem_engine(data[index*number_sample_per_chip+i:], 0)) #sync preamble is chip[0]
        index += number_sample_per_chip
    #plt.plot(len(p[0]), p[0], linestyle='dashed', marker='o')
    #plt.show()
    #print p[0]


def rx(data):
    sync_det(data)
    pass

