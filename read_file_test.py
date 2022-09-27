#!/bin/env python3
import unittest
import fileread

class ReadFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv_file = "testfile.csv"
        self.tsv_file = "testfile.tsv"

# ID file tests
    # if the file reads a csv file
    def test_id_csv(self):
        self.assertEqual(
                fileread.id_file(self.csv_file),
                "CSV",
                "Incorrect file type")

    #if the file reads a tsv file
    def test_id_tsv(self):
        self.assertEqual(
                fileread.id_file(self.tsv_file), 
                "TSV",
                "Incorrect file type")

    #if the file reads a tsv file
    def test_id_unknown(self):
        self.assertEqual(
                fileread.id_file("asdasda"), 
                "UNKNOWN",
                "Incorrect file type")

# READ CSV FILE TESTS

# READ TSV FILE TESTS

# READ FILE TESTS
