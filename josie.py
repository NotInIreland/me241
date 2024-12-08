#josie put your code here!
import numpy as np
import os
print(os.getcwd())



data = np.loadtxt("/Users/josiesoles/Downloads/W flange beams sae table.csv", dtype=str, skiprows=5, delimiter=',')
id = data[:,0]
depth = data[:,1]
width = data[:,2]
wThickness = data[:,3]
fThickness = data[:,4]
weight = data[:,6]
n = len(id)

def I(dimension):
    for i in range(0, n):
        d1 = float(depth[i])
        w1 = float(width[i])
        wt1 = float(wThickness[i])
        ft1 = float(fThickness[i])
        wh = d1-(2*ft1)
        if id[i] == dimension:
            I = 2*((ft1 * (w1**3))/12)+((wh*(wt1**3))/12)
    return I

def W(dimension):
    for i in range(0, len(id)):
        weight1 = weight[i]
        if id[i] == dimension:
            W = float(weight1)
    return W

W('W 27 x 178')


