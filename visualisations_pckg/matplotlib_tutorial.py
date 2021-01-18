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
