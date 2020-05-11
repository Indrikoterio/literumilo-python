#! -*- coding: utf-8
# literumilo_ending.py
#
# Define the grammatical endings (finaĵoj) of Esperanto words.
#
# Author: Klivo Lendon
# Last edit date: 2020-05-01

from .literumilo_entry import *

# Ending
# Defines an Esperanto grammatical ending, and its part of speech.
class Ending:
    def __init__(self, end, pos):
        self.ending = end
        self.length = len(end)
        self.part_of_speech  = pos    # substantive (noun), adjective, verb, etc.

SUB_O  = Ending("o", POS.Substantive)
SUB_ON = Ending("on", POS.Substantive)
SUB_OJ = Ending("oj", POS.Substantive)
SUB_OJN = Ending("ojn", POS.Substantive)
VERB_IS  = Ending("is", POS.Verb)
VERB_AS  = Ending("as", POS.Verb)
VERB_OS  = Ending("os", POS.Verb)
VERB_I  = Ending("i", POS.Verb)
VERB_U  = Ending("u", POS.Verb)
VERB_US = Ending("us", POS.Verb)
ADJ_A = Ending("a", POS.Adjective)
ADJ_AN = Ending("an", POS.Adjective)
ADJ_AJ = Ending("aj", POS.Adjective)
ADJ_AJN = Ending("ajn", POS.Adjective)
ADV_E = Ending("e", POS.Adverb)
ADV_EN = Ending("en", POS.Adverb)

def get_ending(word):
    """This function checks whether the given word has a valid Esperanto ending.
    If it does, an Ending object is returned. In not, it returns None.
    Params:
        esperanto word
    Return
        Ending object
    """
    word_length = len(word)
    if word_length < 3: return None
    last_ch = word[-1]
    if last_ch == "o": return SUB_O
    if last_ch == "a": return ADJ_A
    if last_ch == "e": return ADV_E
    if last_ch == "i": return VERB_I
    if last_ch == "u": return VERB_U
    if last_ch == "s":
         if word_length < 4: return None
         second_last_ch = word[-2]
         if second_last_ch == "a": return VERB_AS
         if second_last_ch == "i": return VERB_IS
         if second_last_ch == "o": return VERB_OS
         if second_last_ch == "u": return VERB_US
    elif last_ch == "n":
         if word_length < 4: return None
         second_last_ch = word[-2]
         if second_last_ch == "o": return SUB_ON
         if second_last_ch == "a": return ADJ_AN
         if second_last_ch == "e": return ADV_EN
         if second_last_ch == "j":
             if word_length < 5: return None
             third_last_ch = word[-3]
             if third_last_ch == "o": return SUB_OJN
             if third_last_ch == "a": return ADJ_AJN
    elif last_ch == "j":
         if word_length < 4: return None
         second_last_ch = word[-2]
         if second_last_ch == "o": return SUB_OJ
         if second_last_ch == "a": return ADJ_AJ
    return None
