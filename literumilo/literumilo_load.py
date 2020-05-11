#! -*- coding: utf-8
# literumilo_load.py
#
# Module to load an Esperanto dictionary for spell checking.
#
# Author: Klivo Lendon
# Last edit date: 2020-05-01
#

import os, sys
import enum

from .literumilo_utils import x_to_accent
from .literumilo_entry import *

DICTIONARY_FN = 'data/vortaro.tsv'
NL = '\n'

def make_dictionary(lines):
    """
    This function takes rows of tab-separated dictionary data and produces a hash map
    which is indexed by morpheme.
   
    A typical row of data is:
    divid	VERBO	N	T	N	KF	NLM	1	R
   
    The columns are:
    morpheme, part of speech, meaning, transitivity, without-ending, with-ending, combinability, rarity, flag.
   
    morpheme - eg. 'divid', 'elefant', 'amik'
    part of speech - SUBST (substantive), VERBO, ADJEKTIVO, etc.
    meaning - eg. ANIMALO, URBO, PERSONO
    transitivity - N/T
    without-ending - SF = Sen Finaĵo (without ending), N = Ne (no)
    with-ending - KF = Kun Finaĵo (with ending), N = Ne (no)
    combinability - LM (limited), NLM (not limited), P (as prefix), S (as suffix)
    rarity - 0 = very common, 4 = rare
    flag - R (root/ morpheme), K (compound), X (eXclude from dictionary)
   
    Params:
       strings of dictionary data
    Return:
       hash map of dictionary data
    """

    esperanto_dictionary = {}

    # Read the dictionary data line by line.
    for line in lines:
        if len(line) < 10: continue    # must be junk
        if line[0] == '#': continue     # skip comments

        parameter_array = line.split('\t')

        if len(parameter_array) < 9:
            print("Dictionary error >>>>>>> {}".format(line))
            continue

        # Make a key.
        morpheme_key = x_to_accent(parameter_array[0]).lower().replace(".", "")
        entry = EspDictEntry(parameter_array)
        # Exclude any lines with a flag of 'X'
        flag = parameter_array[0]
        if entry.flag != "X":
            esperanto_dictionary[morpheme_key] = EspDictEntry(parameter_array)
            #esperanto_dictionary[morpheme_key].display()
        else:
            #print("--------------------- {}".format(parameter_array))
            pass

    return esperanto_dictionary;


def load_dictionary():
    """Read in the Esperanto dictionary file (tab separated values),
    and produce a dictionary, indexed by morpheme.
    """
    lines = []
    this_path = os.path.abspath(os.path.dirname(__file__))
    dict_path = os.path.join(this_path, DICTIONARY_FN)
    with open(dict_path, 'r') as fp:
        for line in fp:
            lines.append(line.strip())
    return make_dictionary(lines)

# ----------------------------------------------------
# Program starts here.

if __name__ == '__main__':
    load_dictionary()
