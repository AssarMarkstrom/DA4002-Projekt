# Product Backlog - MoSCoW

## Sprint I goal: Start working on Read/filter/summary/graphics.

## Sprint II goal: Finish file_handler, filter, summary and graphics. A prototype including using all the files with a super basic interface.

## Sprint III:

## Must Have:
- ***Read Data***:
    - Accept csv, tsv and excel (xls, xlsx) files.
    - Reject files of incorrect format.
    - Detect variable types.
- ***Data manipulation***:
    - User can filter data based on:
    - Column names
    - Row numbers
- ***Data visualisation***:
    - ***Summary***:
        - Median
        - Mean
        - Standard deviation
    - ***Diagrams***:
        - Histogram
        - Bar chart
        - Scatter plot
        - Line graph
        - Pie chart
## Should Have:
- ***Read Data***:
    - Store file.
    - Coverting from object type in pandas.
    - Store original file and filtered copies of that file.
- ***Data manipulation***:
    - User can filter data based on:
    - Specific values
    - Using information from summary to filter on specific values for example min/max.
    - Filter on value intervals
- ***Data visualisation***:
    - ***Summary***:
        - Min
        - Max
        - Unique values
        - Duplicate values
## Could Have:
- ***Read Data***:
    - Users can interactively manipulate troublesome values.
    - User can manually change variable type assignment
    - Undo filtering for x number of times.
- ***Data visualisation***:
    - View data in table for columns.
## Won’t Have:
- ***Read Data***:
    - GUI manipulating values.
    - File converter for other file-types.
