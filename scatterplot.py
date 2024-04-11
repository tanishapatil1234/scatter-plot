import json
import plotly
import plotly.graph_objs as go

# Load the JSON data
data = {
         "1900": {
      "temperature": 25.4,
      "rainfall": 812.6
    },
    "1901": {
      "temperature": 28.7,
      "rainfall": 726.3
    },
    "1902": {
      "temperature": 26.8,
      "rainfall": 543.9
    },
    "1903": {
      "temperature": 22.1,
      "rainfall": 932.5
    },
    "1904": {
      "temperature": 23.9,
      "rainfall": 678.2
    },
    "1905": {
      "temperature": 29.3,
      "rainfall": 818.7
    },
    "1906": {
      "temperature": 27.6,
      "rainfall": 721.8
    },
    "1907": {
      "temperature": 25.8,
      "rainfall": 635.4
    },
    "1908": {
      "temperature": 24.5,
      "rainfall": 756.9
    },
    "1909": {
      "temperature": 26.2,
      "rainfall": 874.3
    },
    "1910": {
      "temperature": 26.9,
      "rainfall": 799.1
    },
    "1911": {
      "temperature": 25.3,
      "rainfall": 903.6
    },
    "1912": {
      "temperature": 24.8,
      "rainfall": 730.7
    },
    "1913": {
      "temperature": 27.4,
      "rainfall": 652.5
    },
    "1914": {
      "temperature": 28.1,
      "rainfall": 802.4
    },
    "1915": {
      "temperature": 25.7,
      "rainfall": 715.9
    },
    "1916": {
      "temperature": 26.5,
      "rainfall": 882.3
    },
    "1917": {
      "temperature": 23.8,
      "rainfall": 679.8
    },
    "1918": {
      "temperature": 22.4,
      "rainfall": 927.4
    },
    "1919": {
      "temperature": 27.2,
      "rainfall": 732.6
    },
    "1920": {
      "temperature": 28.9,
      "rainfall": 809.3
    },
    "1921": {
      "temperature": 26.6,
      "rainfall": 651.7
    },
    "1922": {
      "temperature": 25.4,
      "rainfall": 847.2
    },
    "1923": {
      "temperature": 24.2,
      "rainfall": 708.5
    },
    "1924": {
      "temperature": 26.8,
      "rainfall": 883.9
    },
    "1925": {
      "temperature": 23.7,
      "rainfall": 742.6
    },
    "1926": {
      "temperature": 27.9,
      "rainfall": 809.8
    },
    "1927": {
      "temperature": 28.5,
      "rainfall": 697.2
    },
    "1928": {
      "temperature": 27.3,
      "rainfall": 868.7
    },
    "1929": {
      "temperature": 24.9,
      "rainfall": 775.3
    },
    "1930": {
      "temperature": 25.1,
      "rainfall": 936.4
    },
    "1931": {
      "temperature": 26.3,
      "rainfall": 682.1
    },
    "1932": {
      "temperature": 25.6,
      "rainfall": 845.9
    },
    "1933": {
      "temperature": 27.8,
      "rainfall": 791.7
    },
    "1934": {
      "temperature": 23.5,
      "rainfall": 726.9
    },
    "1935": {
      "temperature": 27.0,
      "rainfall": 908.3
    },
    "1936": {
      "temperature": 24.3,
      "rainfall": 652.4
    },
    "1937": {
      "temperature": 26.2,
      "rainfall": 813.6
    },
    "1938": {
      "temperature": 25.8,
      "rainfall": 735.1
    },
    "1939": {
      "temperature": 24.6,
      "rainfall": 894.7
    },
    "1940": {
      "temperature": 27.1,
      "rainfall": 721.2
    },
    "1941": {
      "temperature": 26.4,
      "rainfall": 829.5
    },
    "1942": {
      "temperature": 25.2,
      "rainfall": 896.8
    },
    "1943": {
      "temperature": 28.3,
      "rainfall": 643.9
    },
    "1944": {
      "temperature": 27.5,
      "rainfall": 774.2
    },
    "1945": {
      "temperature": 24.1,
      "rainfall": 918.4
    },
    "1946": {
      "temperature": 28.8,
      "rainfall": 692.7
    },
    "1947": {
      "temperature": 27.6,
      "rainfall": 846.9
    },
    "1948": {
      "temperature": 25.3,
      "rainfall": 773.5
    },
    "1949": {
      "temperature": 26.9,
      "rainfall": 912.8
    },
    "1950": {
      "temperature": 25.7,
      "rainfall": 735.4
    },
    "1951": {
      "temperature": 26.1,
      "rainfall": 821.7
    },
    "1952": {
      "temperature": 28.4,
      "rainfall": 787.6
    },
    "1953": {
      "temperature": 23.6,
      "rainfall": 903.1
    },
    "1954": {
      "temperature": 27.9,
      "rainfall": 720.2
    },
    "1955": {
      "temperature": 25.5,
      "rainfall": 862.5
    },
    "1956": {
      "temperature": 25.0,
      "rainfall": 753.8
    },
    "1957": {
      "temperature": 26.8,
      "rainfall": 904.7
    },
    "1958": {
      "temperature": 26.6,
      "rainfall": 719.6
    },
    "1959": {
      "temperature": 27.7,
      "rainfall": 875.2
    },
    "1960": {
      "temperature": 24.7,
      "rainfall": 746.8
    },
    "1961": {
      "temperature": 25.9,
      "rainfall": 922.3
    },
    "1962": {
      "temperature": 26.4,
      "rainfall": 798.5
    },
    "1963": {
      "temperature": 25.2,
      "rainfall": 903.8
    },
    "1964": {
      "temperature": 27.0,
      "rainfall": 756.4
    },
    "1965": {
      "temperature": 23.9,
      "rainfall": 874.9
    },
    "1966": {
      "temperature": 28.1,
      "rainfall": 821.1
    },
    "1967": {
      "temperature": 25.3,
      "rainfall": 712.4
    },
    "1968": {
      "temperature": 25.7,
      "rainfall": 853.7
    },
    "1969": {
      "temperature": 24.8,
      "rainfall": 788.9
    },
    "1970": {
      "temperature": 28.6,
      "rainfall": 926.7
    },
    "1971": {
      "temperature": 27.2,
      "rainfall": 759.3
    },
    "1972": {
      "temperature": 26.9,
      "rainfall": 882.4
    },
    "1973": {
      "temperature": 24.4,
      "rainfall": 820.7
    },
    "1974": {
      "temperature": 26.2,
      "rainfall": 734.8
    },
    "1975": {
      "temperature": 26.0,
      "rainfall": 913.2
    },
    "1976": {
      "temperature": 28.3,
      "rainfall": 753.7
    },
    "1977": {
      "temperature": 23.4,
      "rainfall": 855.6
    },
    "1978": {
      "temperature": 24.1,
      "rainfall": 792.4
    },
    "1979": {
      "temperature": 26.8,
      "rainfall": 924.6
    },
    "1980": {
      "temperature": 25.8,
      "rainfall": 784.9
    },
    "1981": {
      "temperature": 27.6,
      "rainfall": 865.3
    },
    "1982": {
      "temperature": 24.9,
      "rainfall": 726.1
    },
    "1983": {
      "temperature": 23.5,
      "rainfall": 931.8
    },
    "1984": {
      "temperature": 25.3,
      "rainfall": 791.5
    },
    "1985": {
      "temperature": 28.0,
      "rainfall": 889.2
    },
    "1986": {
      "temperature": 28.4,
      "rainfall": 738.1
    },
    "1987": {
      "temperature": 26.5,
      "rainfall": 915.7
    },
    "1988": {
      "temperature": 25.1,
      "rainfall": 754.3
    },
    "1989": {
      "temperature": 24.7,
      "rainfall": 870.2
    },
    "1990": {
      "temperature": 27.9,
      "rainfall": 732.9
    },
    "1991": {
      "temperature": 28.7,
      "rainfall": 842.1
    },
    "1992": {
      "temperature": 24.3,
      "rainfall": 927.3
    },
    "1993": {
      "temperature": 25.5,
      "rainfall": 798.6
    },
    "1994": {
      "temperature": 25.6,
      "rainfall": 904.8
    },
    "1995": {
      "temperature": 27.3,
      "rainfall": 755.9
    },
    "1996": {
      "temperature": 24.6,
      "rainfall": 862.2
    },
    "1997": {
      "temperature": 25.8,
      "rainfall": 792.5
    },
    "1998": {
      "temperature": 28.2,
      "rainfall": 914.3
    },
    "1999": {
      "temperature": 26.3,
      "rainfall": 741.8
    },
    "2000": {
      "temperature": 25.0,
      "rainfall": 875.6
    },
    "2001": {
      "temperature": 27.5,
      "rainfall": 734.7
    },
    "2002": {
      "temperature": 28.8,
      "rainfall": 914.5
    },
    "2003": {
      "temperature": 26.4,
      "rainfall": 851.2
    },
    "2004": {
      "temperature": 25.9,
      "rainfall": 721.6
    },
    "2005": {
      "temperature": 24.8,
      "rainfall": 935.4
    },
    "2006": {
      "temperature": 27.7,
      "rainfall": 791.9
    },
    "2007": {
      "temperature": 27.2,
      "rainfall": 862.3
    },
    "2008": {
      "temperature": 25.3,
      "rainfall": 743.8
    },
    "2009": {
      "temperature": 24.5,
      "rainfall": 917.2
    },
    "2010": {
      "temperature": 26.0,
      "rainfall": 772.9
    },
    "2011": {
      "temperature": 27.6,
      "rainfall": 891.5
    },
    "2012": {
      "temperature": 26.5,
      "rainfall": 726.7
    },
    "2013": {
      "temperature": 25.9,
      "rainfall": 935.8
    },
    "2014": {
      "temperature": 28.2,
      "rainfall": 814.2
    },
    "2015": {
      "temperature": 27.4,
      "rainfall": 870.6
    },
    "2016": {
      "temperature": 25.0,
      "rainfall": 751.9
    }
}

# Extract years, temperatures, and rainfalls
years = [int(year) for year in data.keys()]
temperatures = [entry["temperature"] for entry in data.values()]
rainfalls = [entry["rainfall"] for entry in data.values()]

# Create scatter plot trace for temperature
trace_temperature = go.Scatter(
    x=years,
    y=temperatures,
    mode='markers',
    name='Temperature'
)

# Create scatter plot trace for rainfall
trace_rainfall = go.Scatter(
    x=years,
    y=rainfalls,
    mode='markers',
    name='Rainfall'
)

# Define layout
layout = go.Layout(
    title='Temperature and Rainfall Over Years : California',
    xaxis=dict(title='Year'),
    yaxis=dict(title='Value'),
    hovermode='closest'
)

# Create figure object
fig = go.Figure(data=[trace_temperature, trace_rainfall], layout=layout)

# Save the figure as an HTML file
plotly.offline.plot(fig, filename='index.html', auto_open=False)
