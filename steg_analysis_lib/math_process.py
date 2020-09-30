
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import argrelextrema


def find_local_max(hist):
    
    np.set_printoptions(suppress=True)
    
    local_max = argrelextrema(hist, np.greater)
    local_max = np.asarray(local_max).flatten()
    
    #print(hist)
    #print(local_max)
    #plt.plot(hist)
    #plt.plot(local_max, hist[local_max], "x")
    #plt.show()
    
    return local_max


def find_local_min(hist):
    
    np.set_printoptions(suppress=True)
    
    local_min = argrelextrema(hist, np.less)
    local_min = np.asarray(local_min).flatten()
    
    #print(hist)
    #print(local_min)
    #plt.plot(hist)
    #plt.plot(local_min, hist[local_min], "x")
    #plt.show()
    
    return local_min


def calculate_abs_diff_sum(local_extreme):
    
    
    for i, index in enumerate(local_extreme):
        print(i, index)
    
    
    
    
    
    
    
    
    
    
    
    
    

