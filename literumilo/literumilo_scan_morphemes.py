#! -*- coding: utf-8
# literumilo_scan_morphemes.py - contains functions to check the synthesis
# of prefixes, participle endings, and morphemes with limited combinability.
# Suffixes are checked by another module.
#
# A compound word such as 'mis-kompren-it-(a)' consists of 3 morphemes,
# (excluding the grammatical ending), which are stored in a vector called
# morpheme_list. Whether a prefix (mis-) is valid or not depends on the 
# morphemes which come after it. Whether a participle ending (-it ) is valid
# or not depends on the morphemes which come before it.
#
# Note: Some of the functions below may modify the entries in morpheme_list.
#
# Author: Klivo Lendon
# Last edit date: 2020-05-01
#

from .literumilo_entry import *


def check_bo(index, morpheme_list):
    """Check prefix bo-, meaning 'in-law'. Eg. bo-patr-o (father-in-law).
    For a description of parameters see check_acx().
    """

    if index != 0: return False
    difference = morpheme_list.get_last_index() - index

    if difference > 0:       # Make sure at least one morpheme follows.
        next_entry = morpheme_list.get(index + 1)
        if next_entry:
            if next_entry.meaning == Meaning.PARENCO:
                return True
    return False
# check_bo


def check_cis(index, morpheme_list):
    """Check prefix cis-, meaning 'on the near side'.
    Rare. Used for mountains and rivers. Eg. 'cisalpa' (cisalpine).
    For a description of parameters see check_acx().
    """

    if index != 0: return False
    difference = morpheme_list.get_last_index() - index

    if difference > 0:   # Make sure at least one morpheme follows.
        next_entry = morpheme_list.get(index + 1)
        if next_entry:
            meaning = next_entry.meaning
            if meaning == Meaning.RIVERO: return True
            if meaning == Meaning.MONTO: return True
            if meaning == Meaning.MONTARO: return True
    return False
# check_cis


def check_cxi(index, morpheme_list):
    """Check prefix ĉi-, meaning 'this here'. Eg. 'ĉi-vesper-e' (this evening, adv.).
    Valid only for adjectives and adverbs.
    For a description of parameters see check_acx().
    """
    if index == 0:
        type_of_ending = morpheme_list.type_of_ending()
        if type_of_ending == POS.Adjective or type_of_ending == POS.Adverb:
            return True 
    return False
# check_cxi


def check_eks(index, morpheme_list):
    """Check prefix eks-, meaning 'ex-'. Eg. 'eksprezidento' (expresident).
    Valid only for people.
    For a description of parameters see check_acx().
    """
    if index != 0: return False

    last = morpheme_list.get_last_index()
    n = index + 1
    while n <= last:
        entry = morpheme_list.get(n)
        if entry:
            if is_person(entry.meaning): return True
        n += 1
    return False
# check_eks


def check_ge(index, morpheme_list):
    """Check prefix ge-, meaning 'both sexes'. Valid for people and animals.
    Eg. 'ge-student-oj' (male and female students), 'ge-frat-oj' (brothers and sisters).
    For a description of parameters see check_acx().
    """

    if index != 0: return False

    last = morpheme_list.get_last_index()

    n = index + 1
    while n <= last:
        entry = morpheme_list.get(n)
        if entry:
            meaning = entry.meaning
            if is_person(meaning) or is_animal(meaning):
                return True
        n += 1
    return False

# check_ge


def check_kun(index, morpheme_list):
    """Check kun-, meaning 'together with'. Eg. 'kun-ir-is', (went together).
    For a description of parameters see check_acx().
    """

    if index != 0: return False
    if  check_prepositional_prefix(index, morpheme_list): return True

    last = morpheme_list.get_last_index();
    n = index + 1;
    while n <= last:
        entry = morpheme_list.get(n)
        if entry:
            if entry.part_of_speech == POS.Substantive: return True
        n += 1;
    return False
# check_kun


def check_mal(index, morpheme_list):
    """Check prefix mal-, meaning 'un'.
    Eg. 'mal-feliĉ-a' (unhappy), 'mal-kompren-as' (misunderstands).
    For a description of parameters see check_acx().
    """

    if index != 0: return False
    last = morpheme_list.get_last_index()
    type_of_ending = morpheme_list.type_of_ending()

    if last > 0 and \
       (type_of_ending == POS.Verb or \
        type_of_ending == POS.Adjective or \
        type_of_ending == POS.Adverb):
        return True

    n = index + 1
    while n <= last:
        entry = morpheme_list.get(n)
        if entry:
            pos = entry.part_of_speech
            if pos == POS.Verb or \
                pos == POS.SubstantiveVerb or \
                pos == POS.Adjective:
                return True
        n += 1
    return False

# check_mal


def check_ne(index, morpheme_list):
    """Check prefix ne-, meaning 'not'.
    Eg. 'ne-far-ebla', (not doable), 'ne-taŭg-ul-o' (unsuitable person).
    For a description of parameters see check_acx().
    """

    if index != 0: return False
    last = morpheme_list.get_last_index()
    type_of_ending = morpheme_list.type_of_ending();

    if last > 0 and \
        (type_of_ending == POS.Adjective or type_of_ending == POS.Adverb):
        return True

    n = index + 1
    while n <= last:
        entry = morpheme_list.get(n)
        if entry:
            pos = entry.part_of_speech
            if pos == POS.Adjective: return True
            if pos == POS.Participle: return True
            entry_str = entry.morpheme
            if entry_str == "ad": return True   # ne.uz.ad.o, ne.far.ad.o are valid.
            if entry_str == "ec": return True
        n += 1;
    return False

# check_ne


def check_po(index, morpheme_list):
    """Check prefix po-, meaning 'apiece, at a rate of'. (It's complicated.)
    Eg. 'po-pec-e', (by pieces).
    For a description of parameters see check_acx().
    """
    if index != 0: return False
    last = morpheme_list.get_last_index()
    type_of_ending = morpheme_list.type_of_ending()
    if last > 0 and type_of_ending == POS.Adverb: return True
    return False
# check_po


def check_pra(index, morpheme_list):
    """Check prefix pra-, meaning 'prehistoric, ancient, great'.
    Eg. 'pra-ul-o', (ancestor), 'pra-nep-o' (great-grandson), 'pra-hom-o' (primitive man).
    For a description of parameters see check_acx().
    """

    if index != 0: return False
    last = morpheme_list.get_last_index()
    diff = last - index

    if diff > 0:
        next_entry = morpheme_list.get(index + 1)
        if next_entry:
            pos = next_entry.part_of_speech
            if pos == POS.Substantive or pos == POS.SubstantiveVerb: return True

    if diff > 1:
        next_entry = morpheme_list.get(index + 2)
        if next_entry:
            pos = next_entry.part_of_speech
            if pos == POS.Participle: return True
    return False

# check_pra


def check_pseuxdo(index, morpheme_list):
    """Check prefix pseuxdo-, meaning 'false'.
    Eg. 'pseŭdo-scienc-o', (pseudoscience),
    For a description of parameters see check_acx().
    """
    if index != 0: return False

    last = morpheme_list.get_last_index()
    diff = last - index

    if diff > 0:
        next_entry = morpheme_list.get(index + 1)
        if next_entry:
            pos = next_entry.part_of_speech
            if pos == POS.Substantive: return True
            if pos == POS.SubstantiveVerb: return True
            if pos == POS.Adjective: return True
            return False
    return False
# check_pseuxdo


def check_sen(index, morpheme_list):
    """Check sen-, meaning 'without'.
    Eg. 'sen-interes-a' (without interest, uninteresting),
    'sen-hom-ej-o', (a place without people).
    For a description of parameters see check_acx().
    """

    if index != 0: return False
    if  check_prepositional_prefix(index, morpheme_list): return True

    last = morpheme_list.get_last_index()

    last_entry = morpheme_list.get(last)
    if last_entry:
        m = last_entry.morpheme
        if m == "ul": return True
        if m == "aĵ": return True
        if m == "ej": return True
    return False
# check_sen


def check_sin(index, morpheme_list):
    """Check sin-, meaning 'self'. Because this is reflexive,
    it is only attached to transitive verbs.
    Eg. 'sin-kritik-em-a' (tending to criticise his/herself),
    'sin-re-vok-a', (recursive, calling itself).
    For a description of parameters see check_acx().
    """
    if index != 0: return False
    last = morpheme_list.get_last_index()

    n = index + 1
    while n <= last:
        next_entry = morpheme_list.get(n)
        if next_entry:
            if next_entry.transitivity == Transitivity.Transitive: return True
        n += 1
    return False

# check_sin


def check_sub_super_sur(index, morpheme_list):
    """Check prefixes sub- (under) and sur- (on).
    Eg. 'sub-mar-a' (under sea), 'sur-tabl-e', (on the table).
    For a description of parameters see check_acx().
    """
    if  check_prepositional_prefix(index, morpheme_list): return True
    last = morpheme_list.get_last_index()
    type_of_ending = morpheme_list.type_of_ending()

    if last > 0 and \
       (type_of_ending == POS.Substantive or \
        type_of_ending == POS.SubstantiveVerb):
        return True
    return False

# check_sub_super_sur


def check_first(index, morpheme_list):
    """A long prefix, such as 'antaŭ' (before) or 'inter', is valid
    if it is the first morpheme in the list.
    For a description of parameters see check_acx().
    """
    if index == 0: return True
    return False
# check_first


def check_adverbial_prefix(index, morpheme_list):
    """Check adverbial prefixes. Eg. 'for-ir-is', (went away), 'mis-dir-is' (misspoke).
    Adverbs modify a verb root.
    For a description of parameters see check_acx().
    """

    last = morpheme_list.get_last_index()
    type_of_ending = morpheme_list.type_of_ending()

    if last > 0 and type_of_ending == POS.Verb:
        return True

    n = index + 1
    while n <= last:
        entry = morpheme_list.get(n)
        if entry:
            pos = entry.part_of_speech
            if pos == POS.Verb or pos == POS.SubstantiveVerb: return True
        n += 1
    return False
# check_adverbial_prefix

def check_prepositional_prefix(index, morpheme_list):
    """(Reference. PIV 373)
    Eg. 'kun-ir-is', (went together), 'antaŭ-dir-is' (said before).
    For a description of parameters see check_acx().
    """
    last = morpheme_list.get_last_index()
    type_of_ending = morpheme_list.type_of_ending()

    if last > 0 and \
       (type_of_ending == POS.Adjective or type_of_ending == POS.Adverb):
        return True

    n = index + 1
    while n <= last:
        entry = morpheme_list.get(n)
        if entry:
            pos = entry.part_of_speech
            if pos == POS.Verb or pos == POS.SubstantiveVerb:
                return True
        n += 1
    return False

# check_prepositional_prefix


def check_prefix(prefix, index, morpheme_list):
    """Checks synthesis of a prefix.
    Params:
        prefix as string
        index of morpheme in morpheme list
        morpheme list (vector of dictionary entries)
    Return:
        True for valid synthesis, False otherwise
    """
    # Check technical prefixes such as 'hiper' and 'mega'.
    # These are only valid at the front of a word.
    entry = morpheme_list.get(index)
    if entry:
        if entry.part_of_speech == POS.TechPrefix:
            if index == 0: return True
            return False
    else: return False

    if prefix == "al": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "anstataŭ": return check_first(index, morpheme_list)
    if prefix == "antaŭ": return check_first(index, morpheme_list)
    if prefix == "apud": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "bo": return check_bo(index, morpheme_list)
    if prefix == "cis": return check_cis(index, morpheme_list)
    if prefix == "ĉe": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "ĉi": return check_cxi(index, morpheme_list)
    if prefix == "ĉirkaŭ": return check_first(index, morpheme_list)
    if prefix == "de": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "dis": return check_adverbial_prefix(index, morpheme_list)
    if prefix == "dum": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "ek": return check_adverbial_prefix(index, morpheme_list)
    if prefix == "eks": return check_eks(index, morpheme_list)
    if prefix == "ekster": return check_first(index, morpheme_list)
    if prefix == "el": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "en": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "for": return check_adverbial_prefix(index, morpheme_list)
    if prefix == "ge": return check_ge(index, morpheme_list)
    if prefix == "ĝis": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "inter": return check_first(index, morpheme_list)
    if prefix == "kontraŭ": return check_first(index, morpheme_list)
    if prefix == "krom": return check_first(index, morpheme_list)
    if prefix == "kun": return check_kun(index, morpheme_list)
    if prefix == "laŭ": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "mal": return check_mal(index, morpheme_list)
    if prefix == "mis": return check_adverbial_prefix(index, morpheme_list)
    if prefix == "ne": return check_ne(index, morpheme_list)
    if prefix == "per": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "pli": return check_adverbial_prefix(index, morpheme_list)
    if prefix == "po": return check_po(index, morpheme_list)
    if prefix == "por": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "post": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "pra": return check_pra(index, morpheme_list)
    if prefix == "preter": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "pri": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "pro": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "pseŭdo": return check_pseuxdo(index, morpheme_list)
    if prefix == "re": return check_adverbial_prefix(index, morpheme_list)
    if prefix == "retro": return check_first(index, morpheme_list)
    if prefix == "sen": return check_sen(index, morpheme_list)
    if prefix == "sin": return check_sin(index, morpheme_list)
    if prefix == "sub": return check_sub_super_sur(index, morpheme_list)
    if prefix == "super": return check_sub_super_sur(index, morpheme_list)
    if prefix == "sur": return check_sub_super_sur(index, morpheme_list)
    if prefix == "tra": return check_prepositional_prefix(index, morpheme_list)
    if prefix == "trans": return check_prepositional_prefix(index, morpheme_list)
    return False

# check_prefix


def check_limited_synthesis(morpheme, index, morpheme_list):
    """Some morphemes, because they are short, can cause problems for the spell checker.
    To solve the problem,many short morphemes, have limited combinability.
    A limited verb-morpheme may combine only with a suffix and/or a prefix.
    A limited animal-morpheme may combine only with vir-, -in, -id ktp.
    A limited relationship-morpheme (father, brother) may combine only with pra-, ge- or -in.
    A limited ethnicity-morpheme may combine with -in, -land, etc.
    Params:
        morpheme as string
        index of morpheme in morpheme list
        morpheme list (vector of dictionary entries)
    Return:
        true for valid synthesis, false otherwise
    """

    last = morpheme_list.get_last_index()

    entry = morpheme_list.get(index)
    if entry:
        pos = entry.part_of_speech
        meaning = entry.meaning
    else: False

    # If a verb is short it should have only limited combinability (LM).
    # Such verbs can only combine with prefixes, suffixes, and participle
    # endings.
    if pos == POS.Verb or pos == POS.SubstantiveVerb:
        if index > 0:
            prev = morpheme_list.get(index - 1)
            if prev:
                if prev.synthesis != Synthesis.Prefix: return False
        if index < last:
            next = morpheme_list.get(index + 1)
            if next:
                if next.synthesis != Synthesis.Suffix and next.synthesis != Synthesis.Participle:
                    return False
    elif meaning == Meaning.PARENCO:
        if index > 0 :
            prev = morpheme_list.get(index - 1)
            if prev:
                m = prev.morpheme
                if m != "bo" and m != "ge" and m != "pra": return False
        if index < last:
            next = morpheme_list.get(index + 1)
            if next:
                if next.morpheme != "in": return False
    elif is_animal(meaning):
        if index > 0:
            prev = morpheme_list.get(index - 1)
            if prev:
                if prev.morpheme != "vir": return False
        if index < last:
            next = morpheme_list.get(index + 1)
            if next:
                m = next.morpheme
                if m != "in" and m != "id" and m != "aĵ" and m != "ov": return False
    elif meaning == Meaning.ETNO:
        if index > 0:
            prev = morpheme_list.get(index - 1)
            if prev:
                if prev.morpheme != "ge": return False
        if index < last:
            next = morpheme_list.get(index + 1)
            if next:
                m = next.morpheme
                if m != "in" and m != "id" and m != "land" and m != "stil": return False
    return True
# check_limited_synthesis


def valid_separator(pos, index, morpheme_list):
    """Checks synthesis of a separators. (nask-O-tag-o, du-A-foj-e)
    Params:
        part of speech of separator (O = substantive, A = adjective, I = verb)
        index of morpheme in morpheme list
        morpheme list (vector of dictionary entries)
    Return:
        True for valid synthesis, False otherwise
    """
    if index == 0: return False

    # Get part of speech of previous morpheme.
    previous = morpheme_list.get(index - 1)
    if previous:
        previous_pos = previous.part_of_speech
    else: return False

    # type of ending, eg;  nask-o-tag-O  <-- Substantive, du-a-foj-E  <-- Adverb.
    type_of_ending = morpheme_list.type_of_ending()

    # Reconsider this:
    # ''blu.a.ĉiel.o" is an error. An adjective is not joined directly to a substantive.
    if pos == POS.Substantive and previous_pos > POS.Adjective:
        return False
    # "blu.a.blank.o" is an error. Adjective joined to substantive is invalid.
    elif pos == POS.Adjective or pos == POS.Adverb:
        if type_of_ending != POS.Adjective and type_of_ending != POS.Adverb:
            return False
        if previous_pos > POS.Adverb:
            return False
    return True

# valid_separator


def check_participle(index, morpheme_list):
    """Check participle suffixes, Eg. 'naĝ-ant-a' (swimming), 'forges-it-a' (forgotten).
    Note: Passive participle endings can only be attached to transitive verbs.
    Also, the participle ending is not necessarily the last morpheme in a word.
    Words such as 'forges.it.aĵ.o' are sometimes found.
    For a description of parameters see check_acx().
    """

    if index == 0: return False
    last = morpheme_list.get_last_index()

    entry = morpheme_list.get(index)
    if entry:
        participle_string = entry.morpheme
    else: return False

    previous_entry = morpheme_list.get(index - 1)
    if previous_entry:
        previous_string = previous_entry.morpheme
        previous_pos = previous_entry.part_of_speech
        previous_trans = previous_entry.transitivity
    else: return False

    if index < last:
        next_entry = morpheme_list.get(index + 1)
        if next_entry:
            next_string = next_entry.morpheme
        else: return False

    if previous_pos == POS.Verb or previous_pos == POS.SubstantiveVerb:
        if len(participle_string) == 2:  # -it, -at, and -ot are passive participle endings.
            if previous_trans != Transitivity.Transitive: return False
        if index < last:
            if next_string == "aĵ": return True
            if next_string == "ul": return True
            if next_string == "in": return True
            if next_string == "ec": return True
            if next_string == "ar": return True
            return False
        return True

    if previous_string == "antaŭ": return True
    if previous_string == "anstataŭ": return True
    if previous_string == "ĉirkaŭ": return True
    if previous_string == "kontraŭ": return True
    if previous_string == "super": return True

    return False

# check_participle


def scan_morphemes(morpheme_list):
    """Scan the list of morphemes to check the validity of the synthesis.
    This is done after the word is completely divided into morphemes.
    Params:
        list of morphemes (dictionary entries)
    Return:
        True for valid synthesis, False otherwise
    """
    last = morpheme_list.get_last_index()
    if morpheme_list.count_separators() > 1: return False  # Only allow one.

    for index in range(0, last + 1):
        entry = morpheme_list.get(index)
        if entry:
            syn = entry.synthesis
            pos = entry.part_of_speech
            morpheme = entry.morpheme
            if entry.flag == "separator":
                if not valid_separator(pos, index, morpheme_list): return False
        else: return False

        if syn == Synthesis.Prefix:
            if index == last: return False  # A prefix can't be the last morpheme.
            if not check_prefix(morpheme, index, morpheme_list): return False
        elif syn == Synthesis.Participle:
            if not check_participle(index, morpheme_list): return False
        elif syn == Synthesis.Limited:
            if not check_limited_synthesis(morpheme, index, morpheme_list):
                return False

    return True
