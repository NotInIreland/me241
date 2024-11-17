#jacob put your code here!
#test
import numpy as np
import scipy as sp
from sympy import symbols, integrate
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
x, p, c1, c2 = symbols('x, p, c1, c2')
def slopecantilever(x, p):
    m = -p * x
    theta = integrate(m, x) + c1
    return theta

theta = slopecantilever(x, p)


def deflcantilever(x, p):
    deflec = integrate(theta, x) + c2
    return deflec

deflec = deflcantilever(x, p)

thetaval = theta.subs({x: 5, p: 50, c1: 0})
print(thetaval)

deflecval = deflec.subs({x: 5, p: 50, c1:0, c2: 0})
print(deflecval)