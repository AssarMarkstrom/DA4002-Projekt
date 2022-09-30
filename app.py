import fileread as read 
import column_filter as c_filter
import summary as sum

def main():
    df = read.read_file(".\projectdata\helarsprestationer_from_2017.csv")
    df_filtered = c_filter.col_select(df, ['Total'], keep = True)
    print(sum.get_colnames(df_filtered))
    print(sum.show_mean(df_filtered))

if __name__ == '__main__':
    main()