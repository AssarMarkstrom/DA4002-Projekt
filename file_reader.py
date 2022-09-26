"""
Reading and saving files
"""

import pandas as pd

def read_csv(file_path):
    df = pd.read_csv(file_path)
    print(df)



read_csv(r"C:\Users\piagl\Documents\Kurser\DA4002 - Mjukvaruutveckling\DA4002-Projekt")

# def read_tsv(file_path):
        
    
