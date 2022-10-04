from file_handler import *
import pandas as pd

df_1 = read_file("testfiles/testfile.csv")
df_2 = read_file("testfiles/testfile_sum.csv")
df_3 = read_file("testfiles/testfile_semicolon.csv")
print(df_1.dtypes)
