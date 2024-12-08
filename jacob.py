#jacob put your code here!
import numpy as np
import scipy as sp
from sympy import symbols, integrate
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
x, p, c1, c2, c3, c4, m0 = symbols('x p c1 c2 c3 c4 m0')
#This could be our calculated function for the whole function. Just need to create a function that takes use case scenarios and returns the mgiven variable for
#the function to use.
mgiven = x**2
class beamselect:
    def __init__(self, x, p, m0, w, l, E, I):
        self.x = x
        self.p = p
        self.m0 = m0
        self.w = w
        self.l = l
        self.E = E
        self.I = I
    
    def findbeam(x, p, m0, l, w, mgiven, E, I):
        beamtype = input("What type of beam are you solving for? Your options are cantilever(c)")
        beamload = input("What kind of load is on the beam? Your options are intermediate load(IL), uniformly distributed load(UL), triangular distributed load(TDL), and moment(M)")
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

class totalintegral:
    def __init__(self, x, p, m0, w, l):
        self.x = x
        self.p = p
        self.m0 = m0
        self.w = w
        self.l = l
    def slopetotalintegral(x, p, m0):
        m = mgiven
        theta = integrate(m, x) + c1
        return theta
    def deflectotalintegral(x, p, theta, m0):
        deflec = integrate(theta, x) + c2
        return deflec

totalintegral = totalintegral(x, p)
thetatotal = totalintegral.slopetotalintegral(x, p, m0)
deflectotal = totalintegral.deflectotalintegral(x, p, m0, thetatotal)
thetavaltotal = thetatotal.subs({x: 5, p: 50, c1: 0, m0: 500})
deflecvaltotal = deflectotal.subs({x: 5, p: 50, c1:0, c2: 0, m0: 500})
