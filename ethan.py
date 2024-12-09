%matplotlib widget
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import urllib.request
from ipywidgets import interactive
from IPython.display import display

x = np.linspace(0, 2*np.pi, 100)
f1 = np.sin(x) #shear
f2 = np.cos(x) #moment
f3 = np.sin(x) #deflection
f4 = np.cos(x) #slope

fig = plt.figure(figsize=(10, 10))
gs = fig.add_gridspec(3, 2)

L=30
fAt = 15

#beamType = 'simple'
beamType = 'Fixed'

#loadType = 'Point'
loadType = 'UDL'

# Image plot
ax1 = fig.add_subplot(gs[0, :])
fixed = 'https://raw.githubusercontent.com/NotInIreland/me241/refs/heads/main/fixed.png'
img1 = urllib.request.urlopen(fixed)
simple = 'https://raw.githubusercontent.com/NotInIreland/me241/refs/heads/main/simplebeam.png'
img2 = urllib.request.urlopen(simple)

if beamType == 'Fixed':
    img = Image.open(img1)
    title = 'Fixed Beam'
else:
    img = Image.open(img2)
    ax1.set_title('Simple Beam')
    title = 'Simple Beam'

if loadType == 'Point':
    #457 end and 53 start, total lenght is 404
    def update(fAt):
        ArrowXValue = 404 * (fAt / L) + 53
        ax1.clear()
        ax1.imshow(img)
        ax1.set_xticks([])  # Remove x-axis ticks
        ax1.set_yticks([])  # Remove y-axis ticks
        ax1.set_title(title)
        ax1.set_xlabel(f'{L}m Beam')
        arrow_x, arrow_y = ArrowXValue, 130  # Coordinates where the arrow should point
        arm_length = 20  # Length of the horizontal arm
        ax1.plot([arrow_x-1, arrow_x-1], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
        ax1.annotate(
            '   F',  # Text for the arrow
            xy=(arrow_x, arrow_y),  # End point of the arrow
            xytext=(arrow_x, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
            arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
        )
        fig.canvas.draw()
    interactive_plot = interactive(update, fAt=(0, 30, 1))
    display(interactive_plot)
else:
    ax1.clear()
    ax1.imshow(img)
    ax1.set_xticks([])  # Remove x-axis ticks
    ax1.set_yticks([])  # Remove y-axis ticks
    ax1.set_title(title)
    ax1.set_xlabel(f'{L}m Beam')
    arrow_x, arrow_y = 53, 130  # Coordinates where the arrow should point
    arm_length = 20  # Length of the horizontal arm
    ax1.plot([arrow_x-1, arrow_x-1], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+40, arrow_x+40], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+80, arrow_x+80], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+120, arrow_x+120], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+160, arrow_x+160], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+200, arrow_x+200], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+240, arrow_x+240], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+281, arrow_x+281], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+321, arrow_x+321], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+361, arrow_x+361], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    ax1.plot([arrow_x+404, arrow_x+404], [arrow_y-5, arrow_y - 40], color='red', linewidth=2)
    # Plot a straight horizontal line that goes through the back of the arrow arms
    ax1.plot([arrow_x-1, arrow_x+404], [arrow_y-40, arrow_y-40], color='red', linewidth=2)

    ax1.annotate(
        '   F',  # Text for the arrow
        xy=(arrow_x, arrow_y),  # End point of the arrow
        xytext=(arrow_x, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )
    ax1.annotate(
        '   F',  # Text for the arrow
        xy=(arrow_x + 41, arrow_y),  # End point of the arrow
        xytext=(arrow_x+41, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )
    ax1.annotate(
            '   F',  # Text for the arrow
        xy=(arrow_x + 81, arrow_y),  # End point of the arrow
        xytext=(arrow_x+81, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )
    ax1.annotate(
            '   F',  # Text for the arrow
        xy=(arrow_x + 121, arrow_y),  # End point of the arrow
        xytext=(arrow_x+121, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )
    
    ax1.annotate(
            '   F',  # Text for the arrow
        xy=(arrow_x + 161, arrow_y),  # End point of the arrow
        xytext=(arrow_x+161, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )
    ax1.annotate(
            '   F',  # Text for the arrow
        xy=(arrow_x + 201, arrow_y),  # End point of the arrow
        xytext=(arrow_x+201, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )
    ax1.annotate(
            '   F',  # Text for the arrow
        xy=(arrow_x + 241, arrow_y),  # End point of the arrow
        xytext=(arrow_x+241, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )    
    ax1.annotate(
            '   F',  # Text for the arrow
        xy=(arrow_x + 282, arrow_y),  # End point of the arrow
        xytext=(arrow_x+282, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )
    ax1.annotate(
            '   F',  # Text for the arrow
        xy=(arrow_x + 322, arrow_y),  # End point of the arrow
        xytext=(arrow_x+322, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )
    ax1.annotate(
            '   F',  # Text for the arrow
        xy=(arrow_x + 362, arrow_y),  # End point of the arrow
        xytext=(arrow_x+362, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )
    ax1.annotate(
            '   F',  # Text for the arrow
        xy=(arrow_x + 405, arrow_y),  # End point of the arrow
        xytext=(arrow_x+405, arrow_y - 20),  # Start point of the arrow (20 pixels above the end point)
        arrowprops=dict(facecolor='red', shrink=0.05, width=2, headwidth=10)
    )

    fig.canvas.draw()


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

