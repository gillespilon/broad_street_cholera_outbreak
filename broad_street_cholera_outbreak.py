#!/usr/bin/env python3
"""
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
"""

import datasense as ds

colour1 = '#0077bb'
colour2 = '#ee7733'


def main():
    output_url = 'broad_street_cholera.html'
    header_title = 'broad_street_cholera'
    header_id = 'broad-street-cholera'
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    deaths = ds.read_file(file_name='snow_cholera_deaths.csv')
    pumps = ds.read_file(file_name='snow_cholera_pumps.csv')
    file_graph, figsize, legend1, legend2 = (
        'broad_street_cholera_outbreak.svg',
        (8, 6),
        'Deaths',
        'Pumps'
    )
    axis_title, axis_subtitle, x_axis_label, y_axis_label = (
        'Broad Street Cholera Outbreak of 1854',
        'Soho, London, UK',
        'Distance from datum (m)',
        'Distance from datum (m)'
    )
    fig, ax = ds.plot_scatter_scatter_x1_x2_y1_y2(
        figsize=figsize,
        markersize1=3,
        markersize2=3,
        X1=deaths['x'],
        X2=pumps['x'],
        y1=deaths['y'],
        y2=pumps['y'],
        labellegendy1=legend1,
        labellegendy2=legend2,
        colour1=colour1,
        colour2=colour2
    )
    ax.set_title(axis_title + '\n' + axis_subtitle, fontweight='bold')
    ax.set_ylabel(y_axis_label, fontweight='bold')
    ax.set_xlabel(
        xlabel=x_axis_label,
        fontweight='bold'
    )
    ax.legend(frameon=False)
    ds.despine(ax)
    fig.savefig(
        fname=file_graph,
        format='svg'
    )
    ds.html_figure(file_name=file_graph)
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == '__main__':
    main()
