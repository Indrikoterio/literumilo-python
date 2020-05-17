#! -*- coding: utf-8
# literumilo_morpheme_list.py
#
# This file is a list of morphemes for the Esperanto spell checker.
#
# Author: Klivo Lendon
# Last edit date: 2020-05-17

class MorphemeList:
    """The list of morphemes contains up to 9 dictionary entries,
    an index to the last entry, and the word's ending.
    """

    MAX_MORPHEMES = 9    # The maximum number of morphemes in a compound word.

    def __init__(self, ending):
        self.ending = ending
        self.last_index = 0
        self.morphemes =  [None] * self.MAX_MORPHEMES

    def get_last_index(self):
        """Getter for last index."""
        return self.last_index

    def type_of_ending(self):
        """Getter for type (part of speech) of ending. Eg. Substantive, Verb..."""
        return self.ending.part_of_speech

    def display_form(self):
        """This method takes the collected morphemes in the morpheme
       list and returns a string for display, with each morpheme separated
       by a period, eg. 'for.ig.it.a'.
       Return:
           string of morphemes
        """
        morpheme_str = self.morphemes[0].morpheme
        for index in range(1, self.last_index + 1):
            morpheme_str += "." + self.morphemes[index].morpheme
        return morpheme_str + "." + self.ending.ending

    def count_separators(self):
        """This method scans the collected morphemes in morpheme_list
        to determine how many separators vowels there are. For example,
        'last.A.temp.e' has 1 separator vowel (A). (last.temp.e is a little
        harder to pronounce.) This program will only allow one per word.
        Return:
            count of separators
        """
        count = 0
        for index in range(0, self.last_index + 1):
            morph = self.morphemes[index]
            if morph.flag == 'separator': count += 1
        return count

    def get(self, index):
        if (index >= self.MAX_MORPHEMES):
            print("MorphemeList, get(), bad index")
            sys.exit(0)
        return self.morphemes[index]

    def put(self, index, entry):
        if (index >= self.MAX_MORPHEMES):
            print("MorphemeList, put(), bad index")
            sys.exit(0)
        self.last_index = index
        self.morphemes[index] = entry

