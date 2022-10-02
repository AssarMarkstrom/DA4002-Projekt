"""
Summary of file
"""
from fileread import *
from column_filter import *

def get_colnames(df):
    return list(df.columns)
    
def show_head(df):
    """Returns head of DataFrame

    :param df: A DataFrame
    :type df: pandas.DataFrame
    :return: Head of DataFrame
    :rtype: pandas.DataFrame
    """
    head = df.head()
    return head
# Numerical data 
def show_count(df):
    colnames_list = get_colnames(df)
    count = df[colnames_list].count()
    print(count)

def show_mean(df):
    colnames_list = get_colnames(df)
    mean = df[colnames_list].mean()
    print(mean)

def show_median(df):
    colnames_list = get_colnames(df)
    median = df[colnames_list].median()
    print(median)

def show_std(df):
    colname_list = get_colnames(df)
    std = df[colname_list].std()
    print(std)

def show_min(df):
    colnames_list = get_colnames(df)
    min = df[colnames_list].min()
    print(min)

def show_max(df):
    colnames_list = get_colnames(df)
    max = df[colnames_list].max()
    print(max)

"""
Discrete data 
"""
def show_unique_values(df):
    colnames_list = get_colnames(df)
    df_unique = df.drop_duplicates(subset=colnames_list)
    print(df_unique)

def show_unique_values_count(df):
    colnames_list = get_colnames(df)
    df_unique_count = len(df.drop_duplicates(subset=colnames_list))
    print(df_unique_count)

def show_duplicate_values_count(df):
    colnames_list = get_colnames(df)
    df_duplicate_count = len(df) - len(df.drop_duplicates(subset=colnames_list))
    print(df_duplicate_count)

"""
# create df
data_1 = [10,20,30,40,50,60]
data_2 = ["hej", "hej", "då", "asd"] 
df_1 = pd.DataFrame(data_1, columns=['Numbers'])
df_2 = pd.DataFrame(data_2, columns=['text'])
print("---Numerical---")
print(show_full_summary(df_1))
print(show_count(df_1))
print(show_mean(df_1))
print(show_median(df_1))
print(show_std(df_1))
print(show_min(df_1))
print(show_max(df_1))
print("---Discrete---")
print(show_unique_values(df_2))
print(show_unique_values_count(df_2))
print(show_duplicate_values_count(df_2))
"""