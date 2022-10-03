# Product Backlog - MoSCoW
# Sprint II goal: Finish file_handler, filter, summary and graphics. A prototype using all the files with a super basic interface 
## Must Have:
- ***Read Data***:
    - Detect troublesome values.
    -  Accept csv and tsv files.
    - Reject files of incorrect format
    - Detect variable types
    -  Store file.
- ***Data manipulation***:
    - User can filter data based on:
    - column names/number
    - row numbers
    - Specific row values
    - Specific column values
- ***Data visualisation***:
    - ***Summary***:
        - Median
        - Mean
        - Standard deviation
        - Varians
        - Mode
    - ***Diagrams***:
        - Histogram
        - Bar chart
        - Scatter plot
        - Line graph
        - Pie chart
## Should Have:
- ***Read Data***:
    - Handle troublesome values.
    - Accept excel files.
    - Store original file and filtered copies of that file. (Undo)
- ***Data manipulation***:
    - User can filter data based on:
    - Strings or values containing specific char/digits
    - Max/Min
    - Odd Values
    - NA-values.
    - Intervall sorting
- ***Data visualisation***:
    - ***Summary***:
        - Basic summary updated when dataset is filtered.
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
