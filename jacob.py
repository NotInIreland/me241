#jacob put your code here!
import numpy as np #imports
import scipy as sp
from sympy import symbols, integrate, solve, diff
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os
print(os.getcwd())

x, p, c1, c2, c3, c4, m0, w, l, E, I = symbols('x p c1 c2 c3 c4 m0 w l E I') #creates symbols for equations

data = np.loadtxt('https://raw.githubusercontent.com/NotInIreland/me241/refs/heads/main/W%20flange%20beams%20sae%20table.csv', dtype=str, skiprows=5, delimiter=',')
id = data[:,0] #identification
depth = data[:,1]
width = data[:,2]
webThick = data[:,3] #web thickness
fThick = data[:,4] #flange thickness
weight = data[:,6]
dimension = input("What are your beam dimensions? An example input is W 27 x 178")

beamload = input("What kind of load is on the beam? Your options are intermediate load(IL), uniformly distributed load(UL), triangular distributed load(TL), and moment(M)") #allows user to select load type
Ei = float(input("What is young's modulus for this beam (E value)? This is with assumed units of psi")) #asks for young's modulus
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

def slopecalculate(mgiven, E, I): #slope integration of the moment function with respect to x
    return integrate(mgiven / (E * I), x) + c1
     
def defleccalculate(slopeq): #deflection integration of the moment function with respect to x
    return integrate(slopeq, x) + c2 

def values(mgiven, E, I, epointi): #values function to sub in values to remove variables
    slopeq = slopecalculate(mgiven, E, I) #calls slope function
    deflecq = defleccalculate(slopeq) #calls deflection function

    slopeb = slopeq.subs(x, 0) #boundary conditions of function, set up for solving c1
    deflecb = deflecq.subs(x, 0)

    c1val = solve(slopeb, c1)[0] #solves for c1 with boundary conditions
    c2val = solve(deflecb, c2)[0] #colves for c2 with boundary conditions

    slopec = slopeq.subs(c1, c1val) #subs in c1 into function, slopec is purely in variable form at this moment
    deflectionc = deflecq.subs({c1: c1val, c2: c2val}) #same as above, with the exception of subbing in c1 and c2
    slopeval = slopec.subs(x, epointi).evalf() #evaluates the function at the given point of epointi (evalpoint in inches for consistent units) for slope and deflection
    deflecval = deflectionc.subs(x, epointi).evalf() 
    return slopeval, deflecval, slopec, deflectionc #returning both the evaluated functions and the non-evaluated functions


if beamload == 'il': #works for intermediate load
    l1 = float(input("What is the length of the beam (in ft)")) #asking for inputs, changes them into inches
    l1i = l1 * 12
    x1 = float(input("Where is the load on the beam, starting with 0 on the left side (in ft)"))
    x1i = x1 * 12
    p1 = float(input("What is the load on the beam in units of lbs"))

    mgiven = -p * (l - x) #given moment equation for equation form
    evalpoint = float(input("Where would you like to evaluate the deflection at, starting with 0 on the left side (in ft)"))
    epointi = evalpoint * 12
    slopeval, deflecval, slopec, deflectionc = values(mgiven, E, I, epointi) #calling values function with the 4 outputs
    wfrac = W(dimension) #finding the weight of the beam, first calling the lbs/ft value, then multiplying it by the length of the beam in ft for the final weight in lbs
    beamweight = l1 * wfrac
    shear = diff(mgiven, x) #finding the shear functino from the moment value using sympy diff to derive
    slopeval = slopeval.subs({p: p1, l: l1i, E: Ei, I: Iin}) #sub function to remove all variables and obtain a final value
    deflecval = deflecval.subs({p: p1, l: l1i, E: Ei, I: Iin})
    print(f'The weight of the beam is {beamweight}') #code outputs
    print(f'The slope equation is {slopec}') #variable outputs
    print(f'The deflection equation is {deflectionc}')
    print(f'The slope value at the point {evalpoint} is {slopeval}') #numeric outputs
    print(f'The deflection value at the point {evalpoint} is {deflecval}')
    print(f"The moment equation is {mgiven}") #variable moment output
    print(f"The shear equation is {shear}") #shear variable function output
elif beamload == 'ul': #works for uniformly distributed load
    l1 = float(input("What is the length of the beam (in ft)")) #asking for inputs, changes them into inches
    l1i = l1 * 12
    w2 = float(input("What is the magnitude of the distributed load on the beam in units of lbs / ft"))
    w2 = w2 * l1

    mgiven = (-w * (l - x)**2) / 2 #given moment function
    evalpoint = float(input("Where would you like to evaluate the deflection at, starting with 0 on the left side (in ft)"))
    epointi = evalpoint * 12
    slopeval, deflecval, slopec, deflectionc = values(mgiven, E, I, epointi)
    wfrac = W(dimension)
    beamweight = l1 * wfrac #all same as above
    shear = diff(mgiven, x)
    slopeval = slopeval.subs({w: w2, l: l1i, E: Ei, I: Iin})
    deflecval = deflecval.subs({w: w2, l: l1i, E: Ei, I: Iin})

    print(f'The weight of the beam is {beamweight}')
    print(f'The slope equation is {slopec}') #outputs
    print(f'The deflection equation is {deflectionc}')
    print(f'The slope value at the point {evalpoint} is {slopeval}')
    print(f'The deflection value at the point {evalpoint} is {deflecval}')
    print(f"The moment equation is {mgiven}")
    print(f"The shear equation is {shear}")   
elif beamload == 'm': #works for moment equation
    l1 = float(input("What is the length of the beam (in ft)")) #asking for inputs, changes them into inches
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
elif beamload == 'tl': #works for triangle load, rest is same as above minus moment equation
    l1 = float(input("What is the length of the beam (in ft)")) #asking for inputs, changes them into inches
    l1i = l1 * 12
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
else:
    print('You must type a valid input to solve the functions. The input types are listed, and the call values are listed in parenthesis.')

