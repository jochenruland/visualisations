# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

''' This example code has been taken from the Anatomy of Matplotlib Tutorial by Benjamin Root
https://github.com/matplotlib/AnatomyOfMatplotlib/blob/master/AnatomyOfMatplotlib-Part1-Figures_Subplots_and_layouts.ipynb '''

# Tutorial_Plot_#01
# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()

#-------------------------------------------
# Tutorial_Plot_#2
# Nearly the same as Plot_#1 but defines all components of the plot instead
# of using the defaults in the background

#----Equals plt.plot()-----------
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
#--------------------------------

ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0.5, 4.5)
plt.show()

#-------------------------------------------
# Tutorial_Plot_#3
# Same plot as Plot_#2 but usind the pyplot functions and therefore looks cleaner
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
plt.xlim(0.5, 4.5) # corresponds to ax.set_x_lim(0.5, 4.5)
plt.show()

#-------------------------------------------
# Tutorial_Plot_#4
# My first plot - the simple basics
fig = plt.figure() # initialize a figure
ax = fig.add_axes([0,0,1,1]) # add axes to the figure
plt.show()


#-------------------------------------------
# Tutorial_Plot_#5
# A simple plot with subplot and data
fig = plt.figure() # initialize a figure
ax = fig.add_subplot(111) # adds a subplot with the axes to the figure
plt.scatter(np.linspace(0,1,5),np.linspace(0,5,5))
plt.show()

#-------------------------------------------
# Tutorial_Plot_#6
# Definfing the Figure size
fig = plt.figure(figsize=(10,20))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)
# The three lines above can be replaced by the following line
#fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,20))

ax1.bar([1,2,3],[3,4,5]) #Shawing bar (x and y axis)
ax2.barh([0.5,1,2.5],[0,1,2]) #Showing horizontal bar (x and y axis)
ax2.axhline(0.45)
ax1.axvline(0.65)
ax3.scatter(np.linspace(0,1,5),np.linspace(0,5,5))
plt.show()

# Delete `ax3`
#fig.delaxes(ax3)

#-------------------------------------------
