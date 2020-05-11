#! -*- coding: utf-8
# literumilo_check_word.py     - (kontrolu_vorton)
#
# This file has functions which check the spelling of an Esperanto word.
#
# Author: Klivo Lendon
# Last edit date: 2020-05-01
#

import os, sys
from .literumilo_entry import *
from .literumilo_ending import *
from .literumilo_suffix import check_suffix
from .literumilo_morpheme_list import MorphemeList
from .literumilo_scan_morphemes import scan_morphemes
from .literumilo_utils import *
from .literumilo_load import load_dictionary

esperanto_dictionary = load_dictionary()

# AnalysisResult
# 'word' has the original word divided into morphemes, eg. 'mis.dir.it.a'.
# valid is True if the word is a valid Esperanto word. (correctly spelled)

class AnalysisResult:
    def __init__(self, original, word, valid):
        """
        Params:
            original word
            word - divided into morphemes
            valid - True or False
        """
        self.word = restore_capitals(original, word)
        self.valid = valid

def check_synthesis(rest_of_word, dictionary, index, morpheme_list, last_morpheme):
    """check_synthesis (kontrolu sintezon)
    This method checks the synthesis of suffixes when they are found,
    and other morphemes (prefixes, roots) after the word has been
    completely divided, by calling scan_morphemes().
    Params:
        rest of word
        dictionary
        index of morpheme (int)
        list of morphemes
        last_morpheme (t/f)
    Return:
        True if valid, False otherwise
    """

    entry = morpheme_list.get(index)
    if not entry: return False

    syn = entry.synthesis
    morph = entry.morpheme

    if syn == Synthesis.Suffix and not check_suffix(morph, index, morpheme_list):
        return False

    if not last_morpheme:
        # Divide the rest of the word into morphemes.
        if find_morpheme(rest_of_word, dictionary, index + 1, morpheme_list):
            return True
        return False

    if last_morpheme:
        # Check prefixes (and limited morphemes) after the word has been
        # divided, because the validity of a prefix depends on the morphemes
        # which come after it.
        return scan_morphemes(morpheme_list)

    return False
    # end of check_synthesis()


def find_morpheme(rest_of_word, dictionary, index, morpheme_list):
    """find_morpheme (trovu_radikon)
    This function divides a (presumably) compound word into morphemes,
    while checking synthesis. It is recursive.
    Params:
        rest_of_word - the remainder to be analyzed
        dictionary - a map of word data
        index of morpheme (indekso de radiko)
        morpheme_list - holds a list of previously collected morphemes
    Return:
        True for valid synthesis, False for invalid.
    """

    if len(rest_of_word) == 0:
        return False

    if index >= MorphemeList.MAX_MORPHEMES:
        return False

    if index > 0:
        entry = dictionary.get(rest_of_word)
        if entry:
            # Do we allow this morpheme to join with others?
            if entry.synthesis != Synthesis.No:
                morpheme_list.put(index, entry)
                valid = check_synthesis(rest_of_word, dictionary, index, morpheme_list, True)
                if valid: return True

    length_of_word = len(rest_of_word)
    min_length = 2;  # minimum length of a morpheme
    max_length = length_of_word - 2

    # Try to find a valid morpheme, by dividing the rest of the word.
    for size in range(max_length, min_length - 1, -1):
        morpheme = rest_of_word[0:size]
        entry = dictionary.get(morpheme)
        if entry:
            # Do we allow this morpheme to join with others?
            if entry.synthesis != Synthesis.No:
                rest_of_word2 = rest_of_word[size:]  # Careful, rest_of_word != rest_of_word2
                morpheme_list.put(index, entry)
                valid = check_synthesis(rest_of_word2, dictionary, index, morpheme_list, False)
                if valid: return True

    # Sometimes there is a separator (a grammatical ending) between morphemes.
    # This is usually done to aid pronunciation. Instead of 'fingr.montri.', most would
    # write 'fingr.o.montr.i'. Other examples are: ĝust.a.temp.e, unu.a.foj.e, etc.
    # This algorithm will accept one separator per word. It must be 'o', 'a' or 'e'.
    if index == 0 or length_of_word < 3: return False
    separator_entry = EspDictEntry.new_separator(rest_of_word[0])
    if separator_entry:
        morpheme_list.put(index, separator_entry)
        rest_of_word2 = rest_of_word[1:]
        valid = check_synthesis(rest_of_word2, dictionary, index, morpheme_list, False)
        if valid: return True

    return False

def check_word(original_word):
    """This function tests whether a word is correctly spelled.
    Params:
        original word
        dictionary - a map of word data
    Return:
        AnalysisResult
    """

    if len(original_word) == 1:   # Just a letter or hyphen.
        if is_word_char(original_word):
            return AnalysisResult(original_word, original_word, True)
        else:
            return AnalysisResult(original_word, original_word, False)

    # Check for abbreviations, such as n-r.oj, s-in.oj
    if len(original_word) > 2:
        second_char = original_word[1]
        if is_hyphen(second_char):
            entry = esperanto_dictionary.get(original_word)
            if entry:
                return AnalysisResult(original_word, entry.morpheme, True)
            else:
                return AnalysisResult(original_word, original_word, False)

    original_word = remove_hyphens(original_word)

    # Lower case for analysis.
    word = original_word.lower()
    length_of_word = len(word)

    # Exceptions.
    # A few words cause difficulties for the algorithm, especially accusative pronouns.
    # For example, the pronoun 'vin' means 'you' (accusative), but it is also the root for 'wine' (vino).
    # I want the pronoun to divided as 'vi.n' and the beverage to be 'vin.o' (not vi.n.o). The dictionary
    # has 'vin' as a key, but the keys in a dictionary must be unique. To solve this problem, some
    # pronouns (etc.) will be excluded from the dictionary, and handled as exceptions here.

    if length_of_word < 5:
        if (word == "ĝin"): return AnalysisResult(original_word, "ĝi.n", True)
        if (word == "lin"): return AnalysisResult(original_word, "li.n", True)
        if (word == "min"): return AnalysisResult(original_word, "mi.n", True)
        if (word == "sin"): return AnalysisResult(original_word, "si.n", True)
        if (word == "vin"): return AnalysisResult(original_word, "vi.n", True)
        if (word == "lian"): return AnalysisResult(original_word, "li.an", True)
        if (word == "cian"): return AnalysisResult(original_word, "ci.an", True)

    # First, check the dictionary for words which have no
    # grammatical ending, eg. 'ne', 'dum', 'post'.
    entry = esperanto_dictionary.get(word)
    if entry:
        if entry.without_ending == WithoutEnding.Yes:
            return AnalysisResult(original_word, entry.morpheme, True)

    ending = get_ending(word)
    if ending == None:
        return AnalysisResult(original_word, word, False)
    else:
        length = length_of_word - ending.length
        word_without_ending = word[0:length]
        entry = esperanto_dictionary.get(word_without_ending)
        if entry:
            if entry.with_ending == WithEnding.Yes:
                word_with_ending = entry.morpheme + "." + ending.ending
                return AnalysisResult(original_word, word_with_ending, True)
        else:
            # The root was not found. Maybe it's a compound word.
            # Do a morphological analysis.

            # The morpheme list needs the ending for later analysis.
            morpheme_list = MorphemeList(ending)

            valid_word = find_morpheme(word_without_ending, esperanto_dictionary, 0, morpheme_list)

            if valid_word:
                display_form = morpheme_list.display_form()
                return AnalysisResult(original_word, display_form, True)
            else:
                return AnalysisResult(original_word, word, False)

    return AnalysisResult(original_word, word, False)

# check_word
