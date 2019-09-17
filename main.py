import random
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from sorting import *


#Create array and choose sorting algorithm
n = 50 #Number of elements
array = [x for x in range(n)]
random.shuffle(array)
generator = mergeSort(array)
type = "Merge"

#Matplotlib variables
frames = 240
interval = 50
title = "{} Sort".format(type)
file_name = "individual_gifs/{}.mp4".format(type)

#Setup the graph
fig = plt.figure()
plt.title(title)
plt.xticks([])
plt.yticks([])
x = range(1,len(array)+1)
bars = plt.barh(x,array)

#Animation Function
def animate(i):
    y = next(generator)
    for i, b in enumerate(bars):
        b.set_width(y[i])

#Setup for writer
Writer = animation.writers['ffmpeg']
writer = Writer(fps=5)

#Show and save graph
anim=animation.FuncAnimation(fig,animate,repeat=False,blit=False,frames=frames,interval=interval)
#anim.save(file_name, writer=writer)
plt.show()
