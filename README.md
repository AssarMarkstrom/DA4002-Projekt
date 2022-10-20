# DA4002-Projekt

## Data-analysis-tool

An advanced prototype of an application that allows interactive exploration of a multidimensional dataset. With loaded data, the application gives you tools to filter, visualize, and summarize data.

## Description

The purpose of this project is to create a prototype of a data analysis tool that would allow users to interactively explore a multidimensional dataset. The app provides you with tools to filter, visualize, and summarize data using loaded information. The data can be either discrete or continuous, and is given in a column format. Data can be made up of various data types, such as integers, floats, strings, and time. The column always has the specified data type, though. This data can be inputted in various ways, such as CSV, TSV, or Excel. One row of data represents one data point across multiple dimensions. This allows us to view data points from multiple perspectives and understand them better. 

With the data analysis tool, you can set requirements for the data points to display. Numeric data can be filtered by setting ranges and choosing which discrete values to include. This allows you to focus on the data that is most relevant to your needs. Rows that don't meet the selected criteria will be removed. The application's filtering capabilities are interactive and support an exploratory approach. This means that users can filter data to explore different aspects of it. You can change or extend the filter conditions based on the visuals or summary. Filtering is only temporary and you can reset your choices without needing to read the data from the file again. There are many different ways to filter data, limited only by your imagination. The data can be displayed in various ways. 

To understand the distribution of data in a column, you can create a histogram. You can create a scatter plot or a line chart using two columns of numerical data. For discrete data like strings, you might want a bar chart. Data can be summarized in various ways, including through charts, graphs, and tables. For numerical data, you can calculate various measures of central tendency, such as the mean and standard deviation, as well as measures of dispersion such as the median, min, and max. To find the number of unique values for discrete data, simply count the number of different values. The descriptive statistics will update when you filter your data. The purpose of this prototype is to allow multiple views of the same data to be active at the same time, with the views being affected by filtering. The histogram and scatterplot both show the same data, but the histogram highlights certain outliers that you might not notice in the scatterplot. Removing these outliers can affect both visualizations. 

If you filter your data based on what you see in the scatterplot, you will affect both the scatterplot and the other visualization. In order to create the best possible product, we decided to implement several different project tools that we introduced earlier in the course. Regular use of these tools helped us get an overview of the project, identify what needed to be done, and plan the next steps. However, some tools have proven less useful than others, with mixed results and applications.


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
