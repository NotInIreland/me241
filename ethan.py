import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import csv
import urllib.request

x = np.linspace(0, 2*np.pi, 100)
f1 = np.sin(x)
f2 = np.cos(x)
f3 = np.sin(x)
f4 = np.cos(x)
f5 = np.tan(x)

fig = plt.figure(figsize=(12, 12))
gs = fig.add_gridspec(3, 2)

# Image plot
ax1 = fig.add_subplot(gs[0, :])
url = 'https://raw.githubusercontent.com/NotInIreland/me241/refs/heads/main/cantaliver_beam.png'
response = urllib.request.urlopen(url)
img = Image.open(response)
ax1.imshow(img)
ax1.axis('off')  # Hide axes for the image

# Plot sin(x)
ax2 = fig.add_subplot(gs[1, 0])
ax2.plot(x, f1)
ax2.set_title('sin(x)')

# Plot cos(x)
ax3 = fig.add_subplot(gs[1, 1])
ax3.plot(x, f2)
ax3.set_title('cos(x)')

# Plot sin(x)
ax4 = fig.add_subplot(gs[2, 0])
ax4.plot(x, f3)
ax4.set_title('sin(x)')

# Plot cos(x)
ax5 = fig.add_subplot(gs[2, 1])
ax5.plot(x, f4)
ax5.set_title('cos(x)')

plt.tight_layout()
plt.show()

# Read the CSV file
url = 'https://raw.githubusercontent.com/NotInIreland/me241/refs/heads/main/Beam%20Table.csv'
# Read the CSV file with numpy
csv_data = np.genfromtxt(url, delimiter=',', skip_header=1, dtype=None, encoding='utf-8')
# Print the numpy array
print(csv_data)