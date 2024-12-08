#josie put your code here!
import numpy as np
import os
print(os.getcwd())



data = np.loadtxt("/Users/josiesoles/Downloads/W flange beams sae table.csv", dtype=str, skiprows=5, delimiter=',')
id = data[:,0]
d = data[:,1]
w = data[:,2]
wt = data[:,3]
ft = data[:,4]
n = len(id)

def I(dimension):
    for i in range(0, n):
        d1 = float(d[i])
        w1 = float(w[i])
        wt1 = float(wt[i])
        ft1 = float(ft[i])
        if id[i] == dimension:
            i1 = (w1 * (d1**3))/12
            i2 = ((w1-wt1)*((d1 - 2 * ft1)**3))/12
            I = i1 - i2
    return I

I('W 27 x 94')
