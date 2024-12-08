#jacob put your code here!
import numpy as np
import scipy as sp
from sympy import symbols, integrate
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os
print(os.getcwd())

x, p, c1, c2, c3, c4, m0 = symbols('x p c1 c2 c3 c4 m0')

data = np.loadtxt('https://raw.githubusercontent.com/NotInIreland/me241/refs/heads/main/W%20flange%20beams%20sae%20table.csv', dtype=str, skiprows=5, delimiter=',')
id = data[:,0] #identification
depth = data[:,1]
width = data[:,2]
webThick = data[:,3] #web thickness
fThick = data[:,4] #flange thickness
dimension = input('What are the dimensons of this beam')

def I(dimension):
    for i in range(0, len(id)):
        d1 = float(depth[i])
        w1 = float(width[i])
        wt1 = float(webThick[i])
        ft1 = float(fThick[i])
        if id[i] == dimension:
            i1 = (w1 * (d1**3))/12
            i2 = ((w1-wt1)*((d1 - 2 * ft1)**3))/12
            I = i1 - i2
        return I

def findbeam(x, p, m0, l, w, mgiven, E, I):
    beamtype = input("What type of beam are you solving for? Your options are cantilever(c)")
    beamload = input("What kind of load is on the beam? Your options are intermediate load(IL), uniformly distributed load(UL), triangular distributed load(TDL), and moment(M)")
    E = input("What is young's modulus for this beam (E value)? This is with assumed units of psi")
    beamtype = beamtype.lower()
    beamload = beamload.lower()
    if beamtype == 'c':
        if beamload == 'il':
            mgiven = (-p * l - p * x) / (E * I)
            return mgiven
        elif beamload == 'ul':
            mgiven = ((-w * (l - x)**2) / 2) / (E * I)
            return mgiven
        elif beamload == 'm':
            mgiven = (-m0) / (E * I)
            return mgiven
        else:
            return ValueError('You must select a beam and a load type, the given inputs possible are listed in the parenthesis')
       

def slopetotalintegral(x, p, m0, l, w, mgiven, E, I):
    m = mgiven
    theta = integrate(m, x) + c1
    return theta

def deflectotalintegral(x, p, theta, m0):
    deflec = integrate(theta, x) + c2
    return deflec
