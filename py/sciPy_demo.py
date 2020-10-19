
'''
SciPy libs
'''
import numpy as np
import scipy as sp

import random

'''
Pandas Library
-----------------
pandas is a library providing high performance  data stractures and data analysis tools
load data from various sources CSV, database, excel etc....)
'''
import pandas


'''
PyPlotLib  library
-------------------
the library for plots

'''
import matplotlib.pyplot as plt


print ('Hello, world!')

#%%
'''
make Complex signal continues SINE
http://www.mrcolson.com/2015/12/24/Making-Sinusoids-with-Python.html


'''

# signal freq [Hz]
f = 5
# Amplitude
A = 1
# Number of samples
N = 1024
# sample Freq [Hz]
fs = 4000

## Just a sin vs time
t = np.arange(0,20,.01)
phi = np.pi/4
x = A*np.cos(2*np.pi*f*t + phi)
plt.plot(t,x)
plt.axis([0,1,-1,1])
plt.xlabel('time in seconds')
plt.ylabel('amplitude')
plt.show()

