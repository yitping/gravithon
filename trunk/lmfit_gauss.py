import sys, os, linecache, glob
from math import *

import lmfit
import numpy as np

import matplotlib.pyplot as plt

###
def gauss_model(p, x):
    return p['G0'].value + p['A0'].value * np.exp(-((x-p['X0'].value)/(2*p['S0'].value))**2)

errfunc = lambda p, x, y, noise: (gauss_model(p, x) - y)/noise  # error function for lmfit
###
N = 1000
X = np.linspace(-15., 10., N)

G0 = 5.
A0 = 0.8
X0 = 0.1
S0 = 1.2
noise = 0.01

Y = (G0 + A0*np.exp(-((X-X0) / (2*S0))**2)) * (1. + 0.01*np.random.rand(N))

                
#-----------------------
par = lmfit.Parameters()
par.add('G0', value=1.0, min=0., vary=True)
par.add('A0', value=10.0, min=0., vary=True)
par.add('S0', value=0.3, min=0., vary=True)
par.add('X0', value=3.0, min=0., max=10., vary=True)


#-----------------------
result = lmfit.minimize(errfunc, par, args=(X, Y, noise))


print "Initial parameters: ", G0, A0, X0, S0
print "Retrieved parameters: ", str(par['G0'].value)+'+/-'+str(par['X0'].stderr), par['A0'].value, par['X0'].value, par['S0'].value



# Plots
plt.figure()
plt.plot(X, Y, 'b', label='Data')
plt.plot(X, gauss_model(par, X), 'r', label='Best model')
plt.legend(loc='upper right')
plt.show()