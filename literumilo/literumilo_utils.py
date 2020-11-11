#! -*- coding: utf-8
# literumilo_utils.py
#
# This module contains a few utility functions for the Esperanto spell checker 'literumilo'.
#
# Author: Klivo Lendon
# Last edit date: 2020-11-11
#

def accepts_hat(letter):
    """This function tests whether the given letter can accept an accent (hat).
    For example, 'c' can take an accent (ĉ).
    Params: letter
    Result: True if letter is c,g,h,j,s, or u. otherwise False
    """
    if (letter == 'c' or letter == 'C' or letter == 'g' or letter == 'G' or \
        letter == 'h' or letter == 'H' or letter == 'j' or letter == 'J' or \
        letter == 's' or letter == 'S' or letter == 'u' or letter == 'U'):
        return True
    return False

def is_x(letter):
    """This function tests whether the given letter is x or X.
    Params: letter
    Result: True/False
    """
    if letter == 'x' or letter == 'X':
        return True
    return False

def accent_letter(letter):
    """This function puts an Esperanto accent on the given letter.
    Params: letter
    Returns: accented letter
    """
    if letter == 'c': return 'ĉ'
    if letter == 'g': return 'ĝ'
    if letter == 'h': return 'ĥ'
    if letter == 'j': return 'ĵ'
    if letter == 's': return 'ŝ'
    if letter == 'u': return 'ŭ'
    if letter == 'C': return 'Ĉ'
    if letter == 'G': return 'Ĝ'
    if letter == 'H': return 'Ĥ'
    if letter == 'J': return 'Ĵ'
    if letter == 'S': return 'Ŝ'
    if letter == 'U': return 'Ŭ'
    return '?'

def is_word_char(ch):
    """This function returns True for word characters such as 'abc',
    and False for others, such as punctuation and white space.
    """
    if (ch >= 'a' and ch <= 'z'): return True
    if (ch >= 'A' and ch <= 'Z'): return True
    if (ch >= 'À' and ch <= 'ʯ'): return True
    if (ch == '-' or ch == '­'): return True
    return False

def is_hyphen(ch):
    """Returns True for hyphens (0x002D and 0x00AD); False otherwise.
    """
    if (ch == '-' or ch == '­'): return True
    return False

def remove_hyphens(word):
    """Removes hyphens from string.
    """
    return word.replace("-", "").replace("­", "")

def x_to_accent(word):
    """Convert x's in an Esperanto word to accents. In other words,
         convert cx to ĉ, sx to ŝ, etc., for the given word.
    """
    length = len(word)
    new_word = ""
    skip_x = False   # For skipping over x.

    for i in range(0, length):
        if skip_x:
            skip_x = False
            continue
        ch1 = word[i]
        if accepts_hat(ch1):
            if i < (length - 1):
                ch2 = word[i + 1]
                if is_x(ch2):
                    new_word += accent_letter(ch1)
                    skip_x = True
                else:
                    new_word += ch1
            else:
                new_word += ch1
        else:
            new_word += ch1
    return new_word
# --- end of x_to_accent(word)

def restore_capitals(original, analyzed):
    """The Esperanto dictionary (vortaro) has only lower case morphemes, so words
    are converted to lower case for dictionary lookups. It might be useful to
    convert words back to their original case after analysis. For example, an
    analysis of the word  'RIĈULO' will produce 'riĉ.ul.o'. This function will take
    'RIĈULO' and 'riĉ.ul.o' to produce 'RIĈ.UL.O'.
    Params:
         original word
         result of analysis
    Return:
         analyzed result with original case restored
    """
    result = ""
    index = 0
    original_length = len(original)
    # Note: Sometimes a single accented capital letter becomes two codes
    # when converted to lower case. In other words, length of the analyzed
    # word is longer than the original. To avoid an 'out of range' error, when
    # restoring capitals, the index must be compared with the original length.
    for ch in analyzed:
        if ch == ".":
            result += "."
        else:
            if (index < original_length):
                result += original[index]
            else:
                result += ch
            index += 1
    return result
# end of restore_capitals
