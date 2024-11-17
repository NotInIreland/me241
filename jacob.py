#jacob put your code here!
#test
import numpy as np
import scipy as sp
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
def slopecantilever(x, p):
    m = -p * x
    theta = sp.integrate(m)

x = 5
p = 50
slopecantilever(x, p)
