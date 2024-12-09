#jacob put your code here!
import numpy as np
import scipy as sp
from sympy import symbols, integrate, solve
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os
print(os.getcwd())

x, p, c1, c2, c3, c4, m0, w, l = symbols('x p c1 c2 c3 c4 m0 w l')

data = np.loadtxt('https://raw.githubusercontent.com/NotInIreland/me241/refs/heads/main/W%20flange%20beams%20sae%20table.csv', dtype=str, skiprows=5, delimiter=',')
id = data[:,0] #identification
depth = data[:,1]
width = data[:,2]
webThick = data[:,3] #web thickness
fThick = data[:,4] #flange thickness
weight = data[:,6]
dimension = input("What are your beam dimensions? An example input is W 27 x 178")

beamtype = input("What type of beam are you solving for? Your options are cantilever(c)")
beamload = input("What kind of load is on the beam? Your options are intermediate load(IL), uniformly distributed load(UL), and moment(M)")
E = float(input("What is young's modulus for this beam (E value)? This is with assumed units of psi"))
beamtype = beamtype.lower()
beamload = beamload.lower()

def inertia(dimension):
    for i in range(0, len(id)):
        d1 = float(depth[i])
        w1 = float(width[i])
        wt1 = float(webThick[i])
        ft1 = float(fThick[i])
        wh = d1-(2*ft1)
        if id[i] == dimension:
            I = 2*((ft1 * (w1**3))/12)+((wh*(wt1**3))/12)
            break
        else:
            I = 'Unreadable input. Please input dimesion of standard designation including spaces. Example: W # x #.'
    return I

I = inertia(dimension)

def Weight(dimension):
    for i in range(0, len(id)):
        weight1 = weight[i]
        if id[i] == dimension:
            W = float(weight1)
            break
        else:
            W = 'Unreadable input. Please input dimesion of standard designation including spaces. Example: W # x #.'
    return weight

def slopecalculate(mgiven, E, I):
    return integrate(mgiven / (E * I), l) + c1
     
def defleccalculate(slopeq):
    return integrate(slopeq, l) + c2 

def values(mgiven, E, I):
    slopeq = slopecalculate(mgiven, E, I)
    deflecq = defleccalculate(slopeq)

    slopeb = slopeq.subs(x, 0)
    deflecb = deflecq.subs(x, 0)

    c1val = solve(slopeb, c1)[0]
    c2val = solve(deflecb, c2)[0]

    slope = slopeq.subs(c1, c1val)
    deflection = deflecq.subs(c2, c2val)
    
    return slope, deflection

if beamtype == 'c':
    if beamload == 'il':
        l1 = float(input("What is the length of the beam (in ft)"))
        x1 = float(input("Where is the load on the beam, starting with 0 on the left side (in ft)"))
        p1 = float(input("What is the load on the beam in units of lbs"))
        mgiven = -p1 * (l1 - x)
        slope, deflection = values(mgiven, E, I)
        print(f'The slope equation is {slope}')
        print(f'The deflection equation is {deflection}')
    elif beamload == 'ul':
        l2 = float(input("What is the length of the beam (in ft)"))
        x2 = float(input("Where do you want to measure the deflection of the beam (in ft)"))
        w2 = float(input("What is the magnitude of the distributed load on the beam in units of lbs / ft"))
        w2 = w2 * l2
        mgiven = (-w * (l - x)**2) / 2
    elif beamload == 'm':
        l3 = float(input("What is the length of the beam (in ft)"))
        x3 = float(input("Where is the moment on the beam, starting with 0 on the left side (in ft)"))
        m03 = float(input("What is the applied moment on this beam, in units of ft * lbs"))
        mgiven = -m03

