#! -*- coding: utf-8
#
# example.py
# An example program to test the literumilo package.
#
# Cleve (Klivo) Lendon, 2020-05-11

import os

from literumilo import check_word
from literumilo import analyze_string
from literumilo import analyze_file

TEXT = "La Makul-likaono aŭ Hiena likaono, Lycaon pictus, estas kanisedo troviĝanta nur en Afriko."
FILENAME = "example.txt"

def good_or_bad(result):
    """
    Formats the output of check_word.
    Params:
        AnalysisResult
    AnalysisResult has two fields:
        word (str)
        valid (bool)
    """
    if result.valid:
        print("OK> {}".format(result.word))
    else:
        print("Bad> {}".format(result.word))

result = check_word("ĉirkaŭiris")
good_or_bad(result)

result = check_word("ĉirkaŭirs")
good_or_bad(result)

result = analyze_string(TEXT, True)
print(result)

result = analyze_string(TEXT, False)
print(result)

script_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(script_path, FILENAME)

result = analyze_file(file_path, True)
print(result)

result = analyze_file(file_path, False)
print(result)
