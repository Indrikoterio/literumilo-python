#! -*- coding: utf-8
#
# example.py
# An example program to test the literumilo package.
#
# Cleve (Klivo) Lendon, 2020-05-11

import sys, os

#import literumilo
from literumilo import check_word
from literumilo import analyze_file
from literumilo import analyze_string
from literumilo import x_to_accent

TEXT = "Birdoj (Aves) estas klaso de vertebruloj kun ĉirkaŭ 9 ĝis 10 mil vivantaj specioj."
FILENAME = "example.txt"

print(x_to_accent("cxirkaux"))

result = check_word("ĉirkaŭiris")
if result.valid:
    print("OK> {}".format(result.word))
else:
    print("Bad> {}".format(result.word))

result = check_word("ĉirkaŭirs")
if result.valid:
    print("OK> {}".format(result.word))
else:
    print("Bad> {}".format(result.word))

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
