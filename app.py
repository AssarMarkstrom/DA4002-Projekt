from fileread import *
from column_filter import *
from summary import *

def main():
    df = read_file(".\projectdata\helarsprestationer_from_2017.csv")
    print(df)
    df_filtered = col_select(df, ['Total'], keep = True)
    print(df_filtered)
    print(df_filtered.columns[0].mean())


if __name__ == '__main__':
    main()