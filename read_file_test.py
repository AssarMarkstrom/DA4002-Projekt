#!/bin/env python3
import unittest
import fileread

class ReadFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv_semicolon_file =  "testfiles/testfile_semicolon.csv"
        self.csv_file =  "testfiles/testfile.csv"
        self.tsv_file =  "testfiles/testfile.tsv"
        self.xls_file =  "testfiles/testfile.xls"
        self.xlsx_file = "testfiles/testfile.xlsx"

# ID file tests
    # if the id is a csv file, it reads as CSV.
    def test_get_filetype_csv(self):
        self.assertEqual(
                fileread.get_filetype(self.csv_file),
                "CSV",
                "Incorrect file type")

    # if the id is a tsv file, it reads as TSV.
    def test_get_filetype_tsv(self):
        self.assertEqual(fileread.get_filetype(self.tsv_file), 
                "TSV",
                "Incorrect file type")
    
    # if the id isa xls file, it reads as XLS.
    def test_get_filetype_xls(self):
        self.assertEqual(
                fileread.get_filetype(self.xls_file),
                "XLS",
                "Incorrect file type")

    # if the file id is a xlsx file, it reads as XLSX.
    def test_get_filetype_xlsx(self):
        self.assertEqual(
                fileread.get_filetype(self.xlsx_file),
                "XLSX",
                "Incorrect file type")

    # if the id is an unknown file, it reads as UNKNOWN.
    def test_get_filetype_unknown(self):
        self.assertEqual(
                fileread.get_filetype("asdada"),
                "UNKNOWN",
                "Incorrect file type")

    # READ CSV FILE TESTS
    # files with semicolon.
    def test_read_file_csv_semicolon(self):
        pd = fileread.read_file(self.csv_semicolon_file)
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
    
    def test_read_file_csv(self):
       pd = fileread.read_file(self.csv_file)
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
       pd = fileread.read_file(self.tsv_file)
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
       pd = fileread.read_file(self.xls_file)
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
        pd = fileread.read_file(self.xlsx_file)
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
        pd = fileread.read_file("ADASDASDASD")
        self.assertTrue(pd is None)
