# DA4002-Projekt: Data-analysis-tool

![alt text](https://github.com/Natpa333/DA4002-Projekt/blob/main/Images/projectexample.png)

## Figure1: Shows an example of the programs visualisation.

## Description

An advanced prototype of an application that allows interactive exploration of a multidimensional dataset. With loaded data, the application gives you tools to filter, visualize, and summarize data. The data can be either discrete or continuous, and is given in a column format. Data can be made up of various data types, such as integers, floats and strings. This data can be inputted in various ways, such as CSV, TSV, or Excel.

### Filter

With the data analysis tool, you can set requirements for the data points to display. Numeric data can be filtered by setting ranges and choosing which discrete values to include. This allows you to focus on the data that is most relevant to your needs. Rows that don't meet the selected criteria will be removed. The application's filtering capabilities are interactive and support an exploratory approach. This means that users can filter data to explore different aspects of it. You can change or extend the filter conditions based on the visuals or summary. Filtering is only temporary and you can reset your choices without needing to read the data from the file again. There are many different ways to filter data, limited only by your imagination.

### Visualisation and summary

To understand the distribution of data in a column, you can create a histogram. You can create a scatter plot or a line chart using two columns of numerical data. For discrete data like strings, you might want a bar chart. Data can be summarized in various ways, including charts, graphs, and tables. For numerical data, you can calculate various measures such as the mean, median, standard deviation, min and max. For discrete or continuous data you can calculate the # of unique values. The descriptive statistics will update when you filter your data. 

### Notes

The purpose of this prototype is to allow multiple views of the same data to be active at the same time, with the views being affected by filtering. If you filter your data based on what you see in the scatterplot, you will affect both the scatterplot and the other active  visualisation.


## Getting Started

### Dependencies

To install the prerequisites and libraries.
```
pip install requirements.txt
```

### Installing

To download the program clone the repo:
```
git clone https://github.com/Natpa333/DA4002-Projekt.git
```

### Executing program

To run the program type one of the following commands in the terminal:
```
python main.py
```
Or:
```
python3 main.py
```

## Help

For any advise on problems or issues contact one of the authors.

## Authors

Assar Markström
[assarmarkstrom@gmail.com]

Natalija Paunic
[natalijapaunic@hotmail.com]

Pia

Sepehr

## Version History

* 0.1
    * Initial Released

## License

This project is licensed under the [MIT] License - see the `LICENSE.md` file for details
