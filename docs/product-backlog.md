# Product Backlog - MoSCoW

## Sprint I goal: Start working on Read/filter/summary/graphics.

## Sprint II goal: Finish file_handler, filter, summary and graphics. A prototype including using all the files with a super basic interface.

## Sprint III: new protoype, enhetstester, dokumentation, GUI dabble.

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
    - ***Graphics***:
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
    - User can revert back to previous version of the file.
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
    - ***Graphics***
        - Updated in real time when applying filter settings.
## Could Have:
- ***Read Data***:
    - Storing filters or graphs as pictures.
- ***Data visualisation***:
    - GUI for Graphics and Summary.
## Won’t Have:
- Users can interactively manipulate troublesome values.
- User can manually change variable type assignment
- GUI manipulating values.
- File converter for other file-types.
