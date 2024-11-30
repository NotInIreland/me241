#jacob put your code here!
#test
#Could be useful for josie, use this code to call file from given data: 
# a = np.loadtxt('Data.csv', delimiter=',', skiprows = 1, dtype = 'i')
# print(a)
import numpy as np
import scipy as sp
from sympy import symbols, integrate
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
x, p, c1, c2, c3, c4, m0 = symbols('x p c1 c2 c3 c4 m0')
#This could be our calculated function for the whole function. Just need to create a function that takes use case scenarios and returns the mgiven variable for
#the function to use.
mgiven = x**2
class totalintegral:
    def __init__(self, x, p, m0):
        self.x = x
        self.p = p
        self.m0 = m0
    
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
