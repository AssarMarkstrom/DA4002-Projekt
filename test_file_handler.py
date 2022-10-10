#!/bin/env python3
import unittest
import file_handler
import pandas as pd
# a modual that removes files from directory. 
import os


# The setUp sets up differents tests, in this case different,
# testfiles. There is a test data in order to see if, 
# the dataframe works.

class ReadFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv_semicolon_file =  "testfiles/testfile_semicolon.csv"
        self.csv_file =  "testfiles/testfile.csv"
        self.tsv_file =  "testfiles/testfile.tsv"
        self.xls_file =  "testfiles/testfile.xls"
        self.xlsx_file = "testfiles/testfile.xlsx"
       # test data for dataframe. 
        data = {'col1': [1, 2], 'col2': [3, 4]}
        self.df = pd.DataFrame(data=data)
        
# ID file tests
    # if the id is a csv file, it reads as CSV.
    def test_get_filetype_csv(self):
        self.assertEqual(
                file_handler.get_filetype(self.csv_file),
                "CSV",
                "Incorrect file type")

    # if the id is a tsv file, it reads as TSV.
    def test_get_filetype_tsv(self):
        self.assertEqual(file_handler.get_filetype(self.tsv_file), 
                "TSV",
                "Incorrect file type")
    
    # if the id isa xls file, it reads as XLS.
    def test_get_filetype_xls(self):
        self.assertEqual(
                file_handler.get_filetype(self.xls_file),
                "XLS",
                "Incorrect file type")

    # if the file id is a xlsx file, it reads as XLSX.
    def test_get_filetype_xlsx(self):
        self.assertEqual(
                file_handler.get_filetype(self.xlsx_file),
                "XLSX",
                "Incorrect file type")

    # if the id is an unknown file, it reads as UNKNOWN.
    def test_get_filetype_unknown(self):
        self.assertEqual(
                file_handler.get_filetype("asdada"),
                "UNKNOWN",
                "Incorrect file type")

    # READ CSV FILE TESTS
    # files with semicolon.
    def test_read_file_csv_semicolon(self):
        pd = file_handler.read_file(self.csv_semicolon_file)
        self.assertTrue(pd is not None)
        # Expect 11 rows and 9 columns
        self.assertEqual(pd.shape, (10, 9))
        labels = ['Kalenderår', 
                'Kod', 
                'Benämning', 
                'Omfattning', 
                'Enhet', 
                'Nivå inom studieordning', 
                'Kvinnor', 'Män', 'Total']
        self.assertEqual(list(pd.columns), labels)
    # Reads the filename, and verifies the condition as well
    # 
    def test_read_file_csv(self):
       pd = file_handler.read_file(self.csv_file)
       self.assertTrue(pd is not None)
       # Expect 11 rows and 9 columns
       self.assertEqual(pd.shape, (10,9))
       labels = ['Kalenderår',
                'Kod',
                'Benämning',
                'Omfattning',
                'Enhet',
                'Nivå inom studieordning',
                'Kvinnor', 'Män', 'Total']
       self.assertEqual(list(pd.columns), labels)

# READ TSV FILE TESTS
    # files with tabs.
    def test_read_file_tsv(self):
       pd = file_handler.read_file(self.tsv_file)
       self.assertTrue(pd is not None)
       # Expect 11 rows and 9 columns
       self.assertEqual(pd.shape, (10,9))
       labels = ['Kalenderår',
                'Kod',
                'Benämning',
                'Omfattning',
                'Enhet',
                'Nivå inom studieordning',
                'Kvinnor', 'Män', 'Total']
       self.assertEqual(list(pd.columns), labels)

# READ XLS
    # files with xls.
    def test_read_file_xls(self):
       pd = file_handler.read_file(self.xls_file)
       self.assertTrue(pd is not None)
       # Expect 11 rows and 9 columns
       self.assertEqual(pd.shape, (10,9))
       labels = ['Kalenderår',
                'Kod',
                'Benämning',
                'Omfattning',
                'Enhet',
                'Nivå inom studieordning',
                'Kvinnor', 'Män', 'Total']
       self.assertEqual(list(pd.columns), labels)

# READ XLSX FILE TEST
    # files with xlsx.
    def test_read_file_xlsx(self):
        pd = file_handler.read_file(self.xlsx_file)
        self.assertTrue(pd is not None)
        # Expect 11 rows and 9 columns
        self.assertEqual(pd.shape, (10,9))
        labels = ['Kalenderår',
                'Kod',
                'Benämning',
                'Omfattning',
                'Enhet',
                'Nivå inom studieordning',
                'Kvinnor', 'Män', 'Total']
        self.assertEqual(list(pd.columns), labels)

# READ BAD FILE
    # files that are incorrect.
    def test_read_file_bad(self):
        with self.assertRaises(file_handler.FilenameException):
            file_handler.read_file("ADASDASDASD")

# SAVE FILES
# Saves a temporary file in github, and saves.
# Due to os.remove, it removes the files so that,
# it does overflow with saved files.
    def test_save_file_csv(self):
        file_handler.save_file("tmp.csv", self.df)
        df = file_handler.read_file("tmp.csv")
        os.remove("tmp.csv")
        self.assertTrue(df.equals(self.df))

    def test_save_file_tsv(self):  
        file_handler.save_file("tmp.tsv", self.df)
        df = file_handler.read_file("tmp.tsv")
        os.remove("tmp.tsv")
        self.assertTrue(df.equals(self.df))

    def test_save_file_xls(self):
        file_handler.save_file("tmp.xls", self.df)
        df = file_handler.read_file("tmp.xls")
        os.remove("tmp.xls")
        self.assertTrue(df.equals(self.df))

    def test_save_file_xslx(self):
        file_handler.save_file("tmp.xlsx", self.df)
        df = file_handler.read_file("tmp.xlsx")
        os.remove("tmp.xlsx")
        self.assertTrue(df.equals(self.df))
    
    # Testing the made exception.
    def test_save_file_unknown(self):
        with self.assertRaises(file_handler.FilenameException):
                file_handler.save_file("asdasdasd", self.df)
