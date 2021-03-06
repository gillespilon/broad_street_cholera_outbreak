# Broad Street Cholera Outbreak of 1854

## In brevi

There was a severe outbreak of cholera in 1854 in the Soho district of London, England, which killed 616 people over one month. Dr. John Snow and Reverend Henry Whitehead linked the outbreak to contaminated water, identified the index case, and stopped the outbreak by having the Broad Street water pump disabled.

## Data

Download the data sets.

[snow_cholera_deaths.csv](https://drive.google.com/open?id=0BzrdQfHR2I5DSE5NWFZlQXV5VnM). The x-y values are the distances in m from the lower left datum of the map. Each pair represents one death. There are 578 values, slightly less than the 616 actual deaths.

[snow_cholera_pumps.csv](https://drive.google.com/open?id=0BzrdQfHR2I5DSDd2emxObk9HUDA). The x-y values are the distances in m from the lower left datum of the map. Each pair represents one pump. There are 13 values, representing 13 pumps.

## Methodology

Two plots are drawn on the same grid using a scatter plot with pandas.DataFrame.plot.scatter. 

## References

[John Snow site at UCLA](http://www.ph.ucla.edu/epi/snow.html).

[John Snow's cholera data](http://www.math.uah.edu/stat/data/Snow.html)

Johnson, Steven. *Ghost Map*. 2006. Riverhead Books: New York, NY.

[Wikipedia 1854 Broad Street cholera outbreak](https://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak)
