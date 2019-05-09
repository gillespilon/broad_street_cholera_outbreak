#! /usr/bin/env python3

# # Broad Street Cholera Outbreak

# ## In brevi
#
# There was a severe outbreak of cholera in 1854 in the Soho district of London, England, which killed 616 people over one month. Dr. John Snow and Reverence Henry Whitehead linked the outbreak to contaminated water, identified the index case, and stopped the outbreak by having the Broad Street water pump disabled.

# ## Data
#
# Download the data sets.
#
# [snow_cholera_deaths.csv](https://drive.google.com/open?id=0BzrdQfHR2I5DSE5NWFZlQXV5VnM). The x-y values are the distances in m from the lower left datum of the map. Each pair represents one death. There are 578 values, slightly less than the 616 actual deaths.
#
# [snow_cholera_pumps.csv](https://drive.google.com/open?id=0BzrdQfHR2I5DSDd2emxObk9HUDA). The x-y values are the distances in m from the lower left datum of the map. Each pair represents one pump. There are 13 values, representing 13 pumps.

# ## Methodology
#
# Two plots are drawn on the same grid using a scatter plot with pandas.DataFrame.plot.scatter.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

deaths = pd.read_csv('snow_cholera_deaths.csv')
pumps = pd.read_csv('snow_cholera_pumps.csv')

# Define the graph title and subtitle, and the x and y axis labels.
title = 'Broad Street Cholera Outbreak of 1854'
subtitle = 'Soho, London, UK'
yaxislabel = 'Distance from datum (m)'
xaxislabel = 'Distance from datum (m)'


c = cm.Paired.colors
# c[0] c[1] ... c[11]
# See "paired" in "qualitative colormaps"
# https://matplotlib.org/tutorials/colors/colormaps.html


# Create a graph of y v. x distances from a datum for cholera deaths and water pumps.

# Create a single subplot.
ax = plt.subplot(111)
deaths.plot.scatter('x', 'y', legend=True, ax=ax, s=3, label="Deaths",
                    color=c[0]).axis('auto')
pumps.plot.scatter('x', 'y', legend=True, ax=ax, s=3, label="Pumps",
                   color=c[1]).axis('auto')

# Remove the top and right spines.
for spine in 'right', 'top':
    ax.spines[spine].set_color('none')
# Label the graph and axes.
ax.set_title(title + '\n' + subtitle)
ax.set_ylabel(yaxislabel)
ax.set_xlabel(xaxislabel)
# Remove the box around the legend.
ax.legend(frameon=False)
# Save the graph as svg and pdf.
ax.figure.savefig('broad_street_cholera_outbreak.svg', format='svg');
ax.figure.savefig('broad_street_cholera_outbreak.pdf', format='pdf');


# # References
#
# [John Snow site at UCLA](http://www.ph.ucla.edu/epi/snow.html).
#
# [John Snow's cholera data](http://www.math.uah.edu/stat/data/Snow.html)
#
# Johnson, Steven. *Ghost Map*. 2006. Riverhead Books: New York, NY.
#
# [Wikipedia 1854 Broad Street cholera outbreak](https://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak)
