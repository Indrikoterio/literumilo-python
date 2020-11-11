#! -*- coding: utf-8
# literumilo.py
#
# This program is a spell checker and morphological analyzer for Esperanto.
# It can analyze spelling for a single word, or an entire file.
# Please refer to HOW_TO_USE below.
#
# Author: Klivo Lendon
# Last edit date: 2020-11-11
#

from __future__ import print_function

import os, sys
from .literumilo_utils import is_word_char, x_to_accent
from .literumilo_check_word import check_word

HOW_TO_USE = """\nLiterumilo   version: 1.0.8\n
    ----- (Esperanto sekvas.)\n
    This program is a spell checker and morphological analyzer for Esperanto.\n
    To list misspelled words from a file: python literumilo.py file.txt
    To divide words from a file into morphemes: python literumilo.py -m file.txt
    To check the spelling of a single word: python literumilo.py ĉiutage
    Accents can be represented by 'x': python literumilo.py cxiutage\n
    -----\n
    Ĉi tiu programo estas literumilo kaj analizilo de morfemoj por Esperanto.\n
    Por listigi misliterumitajn vortojn de dosiero: python literumilo.py file.txt
    Por dividi vortojn de dosiero laŭ morfemoj: python literumilo.py -m file.txt
    Por kontroli la literumadon de unu vorto: python literumilo.py ĉiutage
    Oni povas anstataŭigi supersignon per 'x': python literumilo.py cxiutage\n
    Klivo <indriko@yahoo.com> 2020
"""

def analyze_file(filename, mode):
    """
    This function reads text from a file and calls analyze_string(),
    which does a morphological analysis or spell check on the text.
    Params:
        file name
        mode - True = morphological analyzer, False = spell checker
    Return:
        analyzed text, or list of misspelled words  (str)
    """

    if not os.path.exists(filename):   # If there is no file.
        print("Cannot find file: {}".format(filename))
        sys.exit(0)

    # Read the file into a string.
    fin = open(filename, 'r')
    if not fin:
        print("Could not open {}.".format(file_or_word))
        sys.exit(0)

    # Read the file into a string.
    s = fin.read()
    fin.close()

    return analyze_string(s, mode)

# ------------------------ analyze_file


def analyze_string(text, mode):
    """
    Analyzes a string of Esperanto text. If the mode is False, this function
    checks the spelling of each word and returns a list of unknown words.
    If the mode is True, the function returns the analyzed text with each
    known word divided into morphemes (separated by periods).
    Params:
        text
        morpheme mode: True = morphological analyzer, False = spell checker
    Return:
        analyzed text, or list of misspelled words (str)
    """

    bad_words = set()    # To output list of misspelled words in spell-check mode.
    new_text = ""   # To output analyzed text in morphological analysis mode (-m).

    in_word = False
    collected_chars = ""
    for ch in text:   # Iterate over each character.
        if is_word_char(ch):
            in_word = True
            collected_chars += ch
        else:
            if in_word:
                result = check_word(collected_chars);
                if mode:
                    new_text += result.word
                else:
                    if not result.valid:
                        bad_words.add(collected_chars)
                collected_chars = ""
            in_word = False
            if mode:
                new_text += ch

    if in_word:
        result = check_word(collected_chars)
        if mode:
            new_text += result.word
        else:
            if not result.valid:
                bad_words.add(collected_chars)
        collected_chars = ""

    if mode:
        return new_text
    else:
        bad_str = ""
        for word in bad_words:
            bad_str += "{}\n".format(word)
        return bad_str

# ------------------------ analyze_string

def main(params):

    if (len(params) < 2):      # If no parameters.
        print(HOW_TO_USE)
        sys.exit(0)

    major = sys.version_info.major
    minor = sys.version_info.minor
    if major < 3:
        print("This program requires Python 3. Your version is {}.{}.".format(major, minor))
        print("Ĉi tiu programo bezonas 'Python 3'. Via versio estas {}.{}.".format(major, minor))
        sys.exit(0)
    
    morpheme_mode = False;
    first_arg = params[1]
    second_arg = ""
    if (len(params) > 2):
        second_arg = params[2]

    file_or_word = first_arg
    if len(params) > 2:
        if first_arg == "-m":
            morpheme_mode = True
            file_or_word = second_arg

    if os.path.exists(file_or_word):   # If there is a file.
        result = analyze_file(file_or_word, morpheme_mode)
        print(result)

    else: # If not a file, must be a word.
        word = x_to_accent(file_or_word)
        result = check_word(word)
        if result.valid:
            print("{} ✓".format(result.word))
        else:
            print("✘{}".format(file_or_word))

        sys.exit(0)

# ----------------------------------------------------
# Program starts here.

if __name__ == '__main__':
    main(sys.argv)
