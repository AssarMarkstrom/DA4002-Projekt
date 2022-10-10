# DA4002-Projekt

## Data-analysis-tool

An advanced prototype of an application that allows interactive exploration of a multidimensional dataset. With loaded data, the application gives you tools to filter, visualize, and summarize data.

## Description

Data is given in a column format and can consist of discrete and continuous data, i.e. we imagine that data is a mixture of integers, floating point numbers, strings, dates, time, geographical coordinates, etc. A column, however, always has a data type. Possible input formats are CSV, TSV, Excel, and others. One row of data corresponds to one data point in several dimensions.

### Filter

It is possible to set requirements for which data points to look at. By setting ranges on numeric data and choosing which discrete values you want, rows that don't match should be filtered out. Filtering is interactive to support an exploratory approach. Informed by a visualisation, you can change or extend the filtering conditions. All filtering is temporary, so you can reset your choices without having to read the data from file again.

### Visualization
The data left after filtering can be visualised in different ways. 
For example:
* To understand the distribution of data in a column of numeric data, I might choose a histogram.
* With two columns of numeric data, you can produce a scatterplot or line chart.
* For discrete data such as strings, a bar chart may be needed.
* If you have geographic data, you can show on a map where the points are located.
* Dates and times can be placed on year wheels and time axes.

### Summary of data
Data can be summarized in many different ways. For numerical data, you can get the mean, standard deviation, median, min and max, etc. How many matching data points do you have? For discrete data, you may want to know the number of unique values. Also the descriptive statistics should be updated when filtering your data.

### Notes
The purpose of this prototype is to be able to have many different views of the same data active at the same time, and for the views to be influenced by the filtering that is done. For example, if you have a histogram and a scatterplot up, you might first be informed by the histogram to remove certain outliers and that filtering affects both visualizations. If you then decide to do another filtering based on what's in your scatterplot, then both visualizations are affected.

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info!

ex. Hubba Bubba 
ex. [@HubbaBubba]

## Version History
ex.
* 0.2
    * Various bug fixes and optimizations

* 0.1
    * Initial Released

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
