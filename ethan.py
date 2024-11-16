#ill put my code here!

# cantaliver beam
%matplotlib ipympl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
img = plt.imread('cantaliver_beam.png')

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(3*x)
ax.plot(x, y)

plt.show()