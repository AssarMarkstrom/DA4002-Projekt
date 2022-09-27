#!/bin/env python3
import unittest
import fileread

class ReadFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv_file = "testfile.csv"
        self.tsv_file = "testfile.tsv"
        self.xls_file = "testfile.xls"
        self.xlsx_file = "testfile.xlsx"

# ID file tests
    # if the id is a csv file, it reads as CSV.
    def test_id_csv(self):
        self.assertEqual(
                fileread.id_file(self.csv_file),
                "CSV",
                "Incorrect file type")

    # if the id is a tsv file, it reads as TSV.
    def test_id_tsv(self):
        self.assertEqual(
                fileread.id_file(self.tsv_file), 
                "TSV",
                "Incorrect file type")
    
    # if the id isa xls file, it reads as XLS.
    def test_id_xls(self):
        self.assertEqual(
                fileread.id_file(self.xls_file),
                "XLS",
                "Incorrect file type")

    # if the file id is a xlsx file, it reads as XLSX.
    def test_id_xlsx(self):
        self.assertEqual(
                fileread.id_file(self.xlsx_file),
                "XLSX",
                "Incorrect file type")

    # if the id is an unknown file, it reads as UNKNOWN.
    def test_id_unknown(self):
        self.assertEqual(
                fileread.id_file("asdada"),
                "UNKNOWN",
                "Incorrect file type")

# READ CSV FILE TESTS

# READ TSV FILE TESTS

# READ XLS OR XLSX

# READ FILE TESTS
