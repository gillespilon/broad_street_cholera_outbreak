#!/usr/bin/env python3

'''
Broad Street cholera outbreak

    time -f '%e' ./broad_street_cholera_outbreak.py
    ./broad_street_cholera_outbreak.py

There was a severe outbreak of cholera in 1854 in the Soho district of London,
England, which killed 616 people over one month. Dr. John Snow and Reverend
Henry Whitehead linked the outbreak to contaminated water, identified the index
case, and stopped the outbreak by having the Broad Street water pump disabled.

[snow_cholera_deaths.csv](https://drive.google.com/
open?id=0BzrdQfHR2I5DSE5NWFZlQXV5VnM).

The x-y values are the distances in m from the lower left datum of the map.
Each pair represents one death. There are 578 values, slightly less than the
616 actual deaths.

[snow_cholera_pumps.csv](https://drive.google.com/
open?id=0BzrdQfHR2I5DSDd2emxObk9HUDA). The x-y values are the distances in m
from the lower left datum of the map. Each pair represents one pump. There are
13 values, representing 13 pumps.

[John Snow site at UCLA](http://www.ph.ucla.edu/epi/snow.html).
[John Snow's cholera data](http://www.math.uah.edu/stat/data/Snow.html)
Johnson, Steven. *Ghost Map*. 2006. Riverhead Books: New York, NY.
[Wikipedia 1854 Broad Street cholera outbreak]
    (https://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak)
'''


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.axes as axes


# https://matplotlib.org/tutorials/colors/colormaps.html
c = cm.Paired.colors


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    There is only one x axis, on the bottom, and one y axis, on the left.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)


def plot_broad_street(df1: pd.DataFrame,
                      legend1: str,
                      df2: pd.DataFrame,
                      legend2: str,
                      title: str,
                      subtitle: str,
                      yaxislabel: str,
                      xaxislabel: str,
                      file_graph: str) -> None:
    fig, ax = plt.subplots(figsize=(12, 12))
    df1.plot.scatter('x', 'y', legend=True, ax=ax, s=3, label=legend1,
                     color=c[0]).axis('auto')
    df2.plot.scatter('x', 'y', legend=True, ax=ax, s=3, label=legend2,
                     color=c[1]).axis('auto')
    despine(ax)
    ax.set_title(title + '\n' + subtitle)
    ax.set_ylabel(yaxislabel)
    ax.set_xlabel(xaxislabel)
    ax.legend(frameon=False)
    ax.figure.savefig(file_graph, format='svg')


if __name__ == '__main__':
    deaths = pd.read_csv('snow_cholera_deaths.csv')
    pumps = pd.read_csv('snow_cholera_pumps.csv')
    legend1 = 'Deaths'
    legend2 = 'Pumps'
    title = 'Broad Street Cholera Outbreak of 1854'
    subtitle = 'Soho, London, UK'
    yaxislabel = 'Distance from datum (m)'
    xaxislabel = 'Distance from datum (m)'
    file_graph = 'broad_street_cholera_outbreak.svg'
    plot_broad_street(deaths, legend1, pumps, legend2, title, subtitle,
                      yaxislabel, xaxislabel, file_graph)
