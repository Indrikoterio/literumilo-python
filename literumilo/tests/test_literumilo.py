#! -*- coding: utf-8
# test_literumilo.py
#
# This module runs a few unit tests for literumilo. From folder 'literumilo' run:
#
# python3 -m unittest tests/test_literumilo.py 
#
# Author: Klivo Lendon
# Last edit date: 2020-05-10
#

import unittest, os

from literumilo import analyze_file
from literumilo_check_word import check_word
from literumilo_utils import x_to_accent

FILENAME = "test.txt"

class TestLiterumilo(unittest.TestCase):
 
    def test_check_word(self):

        result = check_word('forgesitaj')
        self.assertEqual(result.word, 'forges.it.aj')

        word_to_check = x_to_accent('cxiutage')
        result = check_word(word_to_check)
        self.assertEqual(result.word, 'ĉiu.tag.e')

        result = check_word('kuraciisto')
        self.assertEqual(result.valid, False)
        self.assertEqual(result.word, 'kuraciisto')

        result = check_word('n-rojn')
        self.assertEqual(result.word, 'n-r.ojn')

    def test_analyze_file(self):

        script_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(script_path, FILENAME)

        result = analyze_file(file_path, False)
        self.assertEqual(result, 'vortto\n')

        result = analyze_file(file_path, True)
        self.assertTrue("mis.liter.um.it.a" in result)

    # end of test_check_word()

