#! -*- coding: utf-8
# literumilo_suffix.py
#
# This module contains functions to check the synthesis of suffixes.
# A compound word such as 'frenez-ul-ej-(o)', consists of 3 morphemes,
# (excluding the grammatical ending), which are stored in a list called
# morpheme_list. Whether a suffix (-ul, -ej) is valid or not depends
# on the morphemes which come before it.
#
# Note: Some of the functions below may modify the entries in morpheme_list.
#
# Author: Klivo Lendon
# Last edit date: 2020-05-02
#

from .literumilo_entry import *

def check_acx(index, morpheme_list):
    """Check whether suffix -aĉ is valid. Aĉ means bad (quality), unpleasant, ugly.
    If this is the first morpheme in the word, treat it as an adjective. (aĉ-ulo)
    Otherwise, it can follow a substantive, verb, adjective or participle.
    (hund-aĉ-o, kri-aĉ-is, laŭt-aĉ-a)
    Params:
        index of morpheme
        morpheme list (list of dictionary entries)
    Return:
        True if synthesis is valid, False otherwise
    """
    # If aĉ is the first element, it's OK. Treat it as an adjective.
    if index == 0:
        current_entry = morpheme_list.get(index)
        if current_entry:
            current_entry.part_of_speech = POS.Adjective
            return True
        else: return False

    # Aĉ is not first. Get info from previous entry.
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        meaning = previous_entry.meaning
        transitivity = previous_entry.transitivity
    else: return False

    # Aĉ does not change the character of a word.
    # If 'kri-as' is intransitive, then 'kri-aĉ-as' is also intransitive.
    # It is necessary to transfer the POS (Verb, Substantive),
    # transitivity (etc.) from the previous entry to the aĉ entry.
    current_entry = morpheme_list.get(index)
    if current_entry:
        if pos <= POS.Adjective or pos == POS.Participle:
            current_entry.part_of_speech = pos
            current_entry.meaning = meaning
            current_entry.transitivity = transitivity
            return True
    return False
# check_acx


def check_ad(index, morpheme_list):
    """Check suffix -ad.
    Ad, when attached to a substantive (noun), indicates the associated action. Eg. 'martel-ad-o'
    means 'hammering'. When attached to a verb, it indicates the abstract idea of a verb, or
    repetition or long duration. Eg. 'frap-ad-o' means 'hitting', or 'repeated hitting'.
    This suffix is attached to substantives, verbs or substantive-verbs. (kur-ad-is, funebr-ad-as)
    Its part of speech changes to Verb, and it takes the transitivity of the morpheme it follows.
    For a description of parameters see check_acx().
    """

    if index == 0: return False

    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        transitivity = previous_entry.transitivity
    else: return False

    current_entry = morpheme_list.get(index)
    if current_entry and (pos <= POS.Verb):
        current_entry.part_of_speech = POS.Verb
        current_entry.transitivity = transitivity
        return True

    return False
# check_ad


def check_ajx(index, morpheme_list):
    """Check suffix -aĵ, meaning 'thing'.
    This suffix is attached to adjectives, prepositions
    and participles. (blank-aĵ-o, krom-aĵ-o, perd-it-aĵ-o)
    For a description of parameters see check_acx().
    """

    if index == 0: return True

    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        if pos <= POS.Adjective: return True
        if pos == POS.Preposition: return True
        if pos == POS.Participle: return True
    return False

# check_ajx

def check_an(index, morpheme_list):
    """Check suffix -an, meaning 'member of a group'.
    This suffix is attached to substantives, which do not mean 'person'.
    For a description of parameters see check_acx().
    """
    if index == 0: return True
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        meaning = previous_entry.meaning
        if  pos <= POS.SubstantiveVerb:
            if is_person(meaning): return False
            return True
    return False
# check_an

def check_ar(index, morpheme_list):
    """Check suffix -ar (meaning 'a group of something').
    This suffix is attached to substantives and participles.
    (hom-ar-o, aŭskult-ant-ar-o)
    For a description of parameters see check_acx().
    """
    if index == 0: return True
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech;
        if  pos <= POS.SubstantiveVerb or pos == POS.Participle: return True
    return False
# check_ar


def check_ebl(index, morpheme_list):
    """Check suffix -ebl, meaning 'capable of being verb-ed'.
    This suffix is generally attached to transitive verbs.
    Eg. vid-ebl-a, kurac-ebl-a, Xfal-ebl-a
    For a description of parameters see check_acx().
    """
    if index == 0: return True
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech;
        if  pos == POS.Verb or pos == POS.SubstantiveVerb:
            if previous_entry.transitivity == Transitivity.Transitive: return True
    return False
# check_ebl


def check_ec(index, morpheme_list):
    """Check suffix -ec, which expresses quality or state. (alt-ec-o)
    For a description of parameters see check_acx().
    """

    if index == 0: return False

    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
    else: return False

    current_entry = morpheme_list.get(index)
    if current_entry:
        if pos <= POS.SubstantiveVerb or \
            pos == POS.Adjective or \
            pos == POS.Number or \
            pos == POS.Participle:
            current_entry.part_of_speech = POS.Substantive
            return True
    return False

# check_ec()


def check_eg_et(index, morpheme_list):
    """Check suffixes -eg and -et, which augment or diminish a word.
    (laŭt-eg-a, ruĝ-et-a, kri-eg-is, hund-et-o)
    These two suffixes do not change the part of speech, meaning,
    nor transitivity of the previous morpheme, so these are transferred.
    For a description of parameters see check_acx().
    """

    if index == 0: return False

    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech;
        meaning = previous_entry.meaning;
        transitivity = previous_entry.transitivity;
    else: return False

    current_entry = morpheme_list.get(index)
    if current_entry:
        if  pos <= POS.Adjective:
            current_entry.part_of_speech = pos
            current_entry.meaning = meaning
            current_entry.transitivity = transitivity
            return True
    return False

# check_eg_et

def check_ej(index, morpheme_list):
    """Check suffix -ej, (meaning 'place'). Eg. manĝ-ej-o.
    This suffix should not be attached to a morpheme which already
    has a meaning of 'place' (Loko).
    For a description of parameters see check_acx().
    """

    if index == 0: return False

    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        meaning = previous_entry.meaning
        if  pos <= POS.Adjective:
            if meaning == Meaning.LOKO: return False
            return True
    return False

# check_ej


def check_em(index, morpheme_list):
    """Check suffix -em, (meaning 'tendency'). Eg. dorm-em-a
    For a description of parameters see check_acx().
    """

    if index == 0: return False

    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        if  pos <= POS.Adjective:
            return True

    return False

# check_em


def check_end_ind(index, morpheme_list):
    """Check suffixes -ind and -end.
    -ind means, worthy to be (verb)-ed. Eg. vid-ind-a , worthy to be seen.
    -end means, required to be (verb)-ed. Eg. pag-end-a, necessary to be paid.
    These suffixes are normally only applied to transitive verbs. Mir-ind-a is
    an exception.
    For a description of parameters see check_acx().
    """
    if index == 0: return False
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        if previous_entry.transitivity == Transitivity.Transitive:
            return True
    return False
# check_end_ind


def check_er(index, morpheme_list):
    """Check suffix -er
    -er indicates part of a whole, eg. mon-er-o, a coin (piece of money).
    For a description of parameters see check_acx().
    """
    if index == 0: return False
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        morph = previous_entry.morpheme
        if morph == "sup":
            return False   # 'sup.er' is a mistake for 'super'
        if pos <= POS.SubstantiveVerb:
            return True
    return False
# check_er


def check_ik_ing_ism(index, morpheme_list):
    """Check suffixes -ik, -ing, -ism.
    -ik indicates a science, technique, or art, eg. komput-ik-o (computer science).
    -ing indicates a holder, eg. kandel-ing-o (candle holder).
    -ism indicates a doctrine or customary behaviour, eg. alkohol-ism-o (alcoholism).
    These suffixes are normally attached to substantives.
    For a description of parameters see check_acx().
    """
    if index == 0: return False
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        if  pos <= POS.SubstantiveVerb: return True
    return False
# check_ik_ing_ism()


def check_estr(index, morpheme_list):
    """Check suffix -estr, which indicates a leader, eg. urb-estr-o, (a mayor).
    This suffix is attached to substantives. The new word becomes
    a substantive, with a meaning of 'person'.
    For a description of parameters see check_acx().
    """

    if index == 0:
        current_entry = morpheme_list.get(index)
        if current_entry:
            current_entry.part_of_speech = POS.Substantive
            current_entry.meaning = Meaning.PERSONO
            return True
        return False

    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
    else: return False

    current_entry = morpheme_list.get(index)
    if current_entry:
        if  pos <= POS.SubstantiveVerb:
            current_entry.part_of_speech = POS.Substantive
            current_entry.meaning = Meaning.PERSONO
            return True
    return False
# check_estr

def check_id(index, morpheme_list):
    """Check suffix -id, which means 'offspring of'.
    This suffix is attached to animals, eg. kat-id-o (kitten).
    For a description of parameters see check_acx().
    """
    if index == 0: return True
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        meaning = previous_entry.meaning
        if meaning == Meaning.ETNO: return True
        if is_animal(meaning): return True
    return False
# check_id


def check_ig_igx(index, morpheme_list):
    """Check suffixes -ig and -iĝ.
    -ig is a causative suffix, eg. 'star-ig-is' (make to stand).
    -iĝ indicates a change of state, eg. 'griz-iĝ-is' (became grey).
    For a description of parameters see check_acx().
    """
    if index == 0: return False
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        if  pos <= POS.Adverb or pos == POS.Preposition or pos == POS.Prefix:
            return True
    return False
# check_ig_igx


def check_il(index, morpheme_list):
    """Check suffix -il, meaning 'tool'. Eg. ŝraŭb-il-o (screwdriver)
    For a description of parameters see check_acx().
    """
    if index == 0: return True
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        meaning = previous_entry.meaning
        if  (pos == POS.Verb or pos == POS.SubstantiveVerb) and meaning != Meaning.ILO:
            return True
    return False

# check_il


def check_in(index, morpheme_list):
    """Check suffix -in, meaning 'female'. Eg. patr-in-o (mother).
    For a description of parameters see check_acx().
    """
    if index == 0: return True
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        meaning = previous_entry.meaning
        if  is_person(meaning) or is_animal(meaning): return True
    return False
# check_in

def check_ist(index, morpheme_list):
    """Check suffix -ist, meaning 'a professional, supporter of a idea, doctrine, etc.'.
    Eg. Esperant-ist-o (Esperantisto)
    For a description of parameters see check_acx().
    """
    if index == 0: return False
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        meaning = previous_entry.meaning
        if  pos <= POS.Verb and (not is_person(meaning)): return True
    return False
# check_ist


def check_obl_on_op(index, morpheme_list):
    """Check suffixes -obl, -on, -op. These are attached to numbers.
    Eg. du-obl-e (double), du-on-o (a half), du-op-o (a pair).
    For a description of parameters see check_acx().
    """
    if index == 0: return False
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
       if previous_entry.part_of_speech == POS.Number:
           return True
    return False
# check_obl_on_op

def check_uj(index, morpheme_list):
    """Check suffix -uj, meaning 'a container, a fruit bearing tree, a country'.
    Eg. cindr-uj-o (ashtray), pom-uj-o (apple tree), Angl-uj-o (England).
    For a description of parameters see check_acx().
    """
    if index == 0: return False
    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        meaning = previous_entry.meaning
        if  pos <= POS.SubstantiveVerb and meaning != Meaning.ARBO:
            return True
    return False
# check_uj

def check_ul(index, morpheme_list):
    """Check suffix -ul, meaning 'a person'. Eg. povr-ul-o (poor person).
    Note: This suffix will be allowed to attach to a participle ending,
    eg., 'frap.it.ul.o', although this may be redundant.
    For a description of parameters see check_acx().
    """
    if index == 0: return True

    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        pos = previous_entry.part_of_speech
        meaning = previous_entry.meaning
    else: return False

    if  pos == POS.Participle: return True
    if  pos <= POS.Adjective and not is_person(meaning): return True
    if  pos == POS.Preposition: return True
    return False

# check_ul

def check_suffix(suffix, index, morpheme_list):
    """Checks synthesis of suffixes.
    Params:
        suffix as string
        index of morpheme in morpheme list
        list of morphemes (dictionary entries)
    Return:
        true for valid synthesis, false otherwise
    """
    if suffix == "aĉ": return check_acx(index, morpheme_list)
    if suffix == "ad": return check_ad(index, morpheme_list)
    if suffix == "aĵ": return check_ajx(index, morpheme_list)
    if suffix == "an": return check_an(index, morpheme_list)
    if suffix == "ar": return check_ar(index, morpheme_list)
    if suffix == "ebl": return check_ebl(index, morpheme_list)
    if suffix == "ec": return check_ec(index, morpheme_list)
    if suffix == "eg": return check_eg_et(index, morpheme_list)
    if suffix == "et": return check_eg_et(index, morpheme_list)
    if suffix == "ej": return check_ej(index, morpheme_list)
    if suffix == "em": return check_em(index, morpheme_list)
    if suffix == "end": return check_end_ind(index, morpheme_list)
    if suffix == "ind": return check_end_ind(index, morpheme_list)
    if suffix == "er": return check_er(index, morpheme_list)
    if suffix == "ik": return check_ik_ing_ism(index, morpheme_list)
    if suffix == "ing": return check_ik_ing_ism(index, morpheme_list)
    if suffix == "ism": return check_ik_ing_ism(index, morpheme_list)
    if suffix == "estr": return check_estr(index, morpheme_list)
    if suffix == "id": return check_id(index, morpheme_list)
    if suffix == "ig": return check_ig_igx(index, morpheme_list)
    if suffix == "iĝ": return check_ig_igx(index, morpheme_list)
    if suffix == "il": return check_il(index, morpheme_list)
    if suffix == "in": return check_in(index, morpheme_list)
    if suffix == "ist": return check_ist(index, morpheme_list)
    if suffix == "obl": return check_obl_on_op(index, morpheme_list)
    if suffix == "on": return check_obl_on_op(index, morpheme_list)
    if suffix == "op": return check_obl_on_op(index, morpheme_list)
    if suffix == "uj": return check_uj(index, morpheme_list)
    if suffix == "ul": return check_ul(index, morpheme_list)
    return False
