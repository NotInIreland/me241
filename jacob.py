#jacob put your code here!
import numpy as np
import scipy as sp
from sympy import symbols, integrate, solve, diff
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os
print(os.getcwd())

x, p, c1, c2, c3, c4, m0, w, l, E, I = symbols('x p c1 c2 c3 c4 m0 w l E I')

data = np.loadtxt('https://raw.githubusercontent.com/NotInIreland/me241/refs/heads/main/W%20flange%20beams%20sae%20table.csv', dtype=str, skiprows=5, delimiter=',')
id = data[:,0] #identification
depth = data[:,1]
width = data[:,2]
webThick = data[:,3] #web thickness
fThick = data[:,4] #flange thickness
weight = data[:,6]
dimension = input("What are your beam dimensions? An example input is W 27 x 178")

beamtype = input("What type of beam are you solving for? Your options are cantilever(c)")
beamload = input("What kind of load is on the beam? Your options are intermediate load(IL), uniformly distributed load(UL), triangular distributed load(TL), and moment(M)")
Ei = float(input("What is young's modulus for this beam (E value)? This is with assumed units of psi"))
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

Iin = inertia(dimension)

def W(dimension):
    for i in range(0, len(id)):
        weight1 = weight[i]
        if id[i] == dimension:
            W = float(weight1)
            break
        else:
            W = 'Unreadable input. Please input dimesion of standard designation including spaces. Example: W # x #.'
    return W

def slopecalculate(mgiven, E, I):
    return integrate(mgiven / (E * I), x) + c1
     
def defleccalculate(slopeq):
    return integrate(slopeq, x) + c2 

def values(mgiven, E, I, epointi):
    slopeq = slopecalculate(mgiven, E, I)
    deflecq = defleccalculate(slopeq)

    slopeb = slopeq.subs(x, 0)
    deflecb = deflecq.subs(x, 0)

    c1val = solve(slopeb, c1)[0]
    c2val = solve(deflecb, c2)[0]

    slopec = slopeq.subs(c1, c1val)
    deflectionc = deflecq.subs({c1: c1val, c2: c2val})
    slopeval = slopec.subs(x, epointi).evalf()
    deflecval = deflectionc.subs(x, epointi).evalf()
    return slopeval, deflecval, slopec, deflectionc

if beamtype == 'c':
    if beamload == 'il':
        l1 = float(input("What is the length of the beam (in ft)"))
        l1i = l1 * 12
        x1 = float(input("Where is the load on the beam, starting with 0 on the left side (in ft)"))
        x1i = x1 * 12
        p1 = float(input("What is the load on the beam in units of lbs"))

        mgiven = -p * (l - x)
        evalpoint = float(input("Where would you like to evaluate the deflection at, starting with 0 on the left side (in ft)"))
        epointi = evalpoint * 12
        slopeval, deflecval, slopec, deflectionc = values(mgiven, E, I, epointi)
        wfrac = W(dimension)
        beamweight = l1 * wfrac
        shear = diff(mgiven, x)
        slopeval = slopeval.subs({p: p1, l: l1i, E: Ei, I: Iin})
        deflecval = deflecval.subs({p: p1, l: l1i, E: Ei, I: Iin})
        print(f'The weight of the beam is {beamweight}')
        print(f'The slope equation is {slopec}')
        print(f'The deflection equation is {deflectionc}')
        print(f'The slope value at the point {evalpoint} is {slopeval}')
        print(f'The deflection value at the point {evalpoint} is {deflecval}')
        print(f"The moment equation is {mgiven}")
        print(f"The shear equation is {shear}")
    elif beamload == 'ul':
        l1 = float(input("What is the length of the beam (in ft)"))
        l1i = l1 * 12
        x1 = float(input("Where do you want to measure the deflection of the beam (in ft)"))
        x1i = x1 * 12
        w2 = float(input("What is the magnitude of the distributed load on the beam in units of lbs / ft"))
        w2 = w2 * l1

        mgiven = (-w * (l - x)**2) / 2
        evalpoint = float(input("Where would you like to evaluate the deflection at, starting with 0 on the left side (in ft)"))
        epointi = evalpoint * 12
        slopeval, deflecval, slopec, deflectionc = values(mgiven, E, I, epointi)
        wfrac = W(dimension)
        beamweight = l1 * wfrac
        shear = diff(mgiven, x)
        slopeval = slopeval.subs({w: w2, l: l1i, E: Ei, I: Iin})
        deflecval = deflecval.subs({w: w2, l: l1i, E: Ei, I: Iin})

        print(f'The weight of the beam is {beamweight}')
        print(f'The slope equation is {slopec}')
        print(f'The deflection equation is {deflectionc}')
        print(f'The slope value at the point {evalpoint} is {slopeval}')
        print(f'The deflection value at the point {evalpoint} is {deflecval}')
        print(f"The moment equation is {mgiven}")
        print(f"The shear equation is {shear}")   
    elif beamload == 'm':
        l1 = float(input("What is the length of the beam (in ft)"))
        l1i = l1 * 12
        x1 = float(input("Where is the moment on the beam, starting with 0 on the left side (in ft)"))
        x1i = x1 * 12
        m03 = float(input("What is the applied moment on this beam, in units of ft * lbs"))
        m03i = m03 * 12

        mgiven = -m0
        evalpoint = float(input("Where would you like to evaluate the deflection at, starting with 0 on the left side (in ft)"))
        epointi = evalpoint * 12
        slopeval, deflecval, slopec, deflectionc = values(mgiven, E, I, epointi)
        wfrac = W(dimension)
        beamweight = l1 * wfrac
        shear = diff(mgiven, x)
        slopeval = slopeval.subs({m0: m03i, l: l1i, E: Ei, I: Iin})
        deflecval = deflecval.subs({m0: m03i, l: l1i, E: Ei, I: Iin})

        print(f'The weight of the beam is {beamweight}')
        print(f'The slope equation is {slopec}')
        print(f'The deflection equation is {deflectionc}')
        print(f'The slope value at the point {evalpoint} is {slopeval}')
        print(f'The deflection value at the point {evalpoint} is {deflecval}')
        print(f"The moment equation is {mgiven}")
        print(f"The shear equation is {shear}")
    elif beamload == 'tl':
        l1 = float(input("What is the length of the beam (in ft)"))
        l1i = l1 * 12
        x1= float(input("Where do you want to measure the deflection of the beam (in ft)"))
        x1i = x1 * 12
        w2 = float(input("What is the magnitude of the distributed load on the beam in units of lbs / ft"))
        w2 = w2 * l1

        mgiven = (-1 / 6) * w * (x**3 / l)
        evalpoint = float(input("Where would you like to evaluate the deflection at, starting with 0 on the left side (in ft)"))
        epointi = evalpoint * 12
        slopeval, deflecval, slopec, deflectionc = values(mgiven, E, I, epointi)
        wfrac = W(dimension)
        beamweight = l1 * wfrac
        shear = diff(mgiven, x)
        slopeval = slopeval.subs({w: w2, l: l1i, E: Ei, I: Iin})
        deflecval = deflecval.subs({w: w2, l: l1i, E: Ei, I: Iin})

        print(f'The weight of the beam is {beamweight}')
        print(f'The slope equation is {slopec}')
        print(f'The deflection equation is {deflectionc}')
        print(f'The slope value at the point {evalpoint} is {slopeval}')
        print(f'The deflection value at the point {evalpoint} is {deflecval}')
        print(f"The moment equation is {mgiven}")
        print(f"The shear equation is {shear}.")

