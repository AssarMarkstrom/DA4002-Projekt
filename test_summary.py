#!/bin/env python3
import unittest
from fileread import *
from summary import *

class TestSummary(unittest.TestCase):
    def setUp(self):
        self.testfile_sum =  "testfiles/testfile_sum.csv"
        self.df = read_file(self.testfile_sum)
    
    def test_get_colnames(self):
        self.assertEqual(get_colnames(self.df), list(self.df.head(1)))
    
    def test_show_full_summary(self):
        self.assertIsNotNone(show_full_summary(self.df))

    def test_show_head(self):
        self.assertTrue(
                len(show_head(self.df)) <= 5)

   
