#jacob put your code here!
#test
import numpy as np
import scipy as sp
from sympy import symbols, integrate
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
x, p, c1, c2, c3, c4, m0 = symbols('x p c1 c2 c3 c4 m0')
class Cantileverpe:
    def __init__(self, x, p):
        self.x = x
        self.p = p

    def slopecantilever(x, p):
        m = -p * x
        theta = integrate(m, x) + c1
        return theta

    def deflcantilever(x, p, theta):
        deflec = integrate(theta, x) + c2
        return deflec
  
cantileverpe = Cantileverpe(x, p)
thetape = Cantileverpe.slopecantilever(x, p)
deflecpe = Cantileverpe.deflcantilever(x, p, thetape)
thetavalpe = thetape.subs({x: 5, p: 50, c1: 0})
print(thetavalpe)

deflecvalpe = deflecpe.subs({x: 5, p: 50, c1:0, c2: 0})
print(deflecvalpe)

class Cantilevermome:
    def __init__(self, x, p):
        self.x = x
        self.p = p
        self.m0 = m0

    def slopecantilevermome(x, p, m0):
        m = -m0
        theta = integrate(m, x) + c1
        return theta
    
    def defleccantilevermome(x, p, theta, m0):
        deflec = integrate(theta, x) + c2
        return deflec
    
cantilevermome = Cantilevermome(x, p)
thetamome = Cantilevermome.slopecantilevermome(x, p, m0)
deflecmome = Cantilevermome.defleccantilevermome(x, p, thetamome, m0)
thetavalmome = thetamome.subs({x: 5, p: 50, c1: 0, m0: 500})
deflecvalmome = deflecmome.subs({x: 5, p: 50, c1:0, c2: 0, m0: 500})
print(thetavalmome)
print(deflecvalmome)

        
#Could be useful for josie, use this code to call file from given data: 
# a = np.loadtxt('Data.csv', delimiter=',', skiprows = 1, dtype = 'i')
# print(a)
