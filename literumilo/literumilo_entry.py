#! -*- coding: utf-8
# literumilo_entry.py
#
# This file defines an entry for the Esperanto dictionary.
#
# Author: Klivo Lendon
# Last edit date: 2020-05-01
#

import sys

from .literumilo_utils import *
import enum

# Part of Speech
class POS:
    Substantive = 1   # = noun
    SubstantiveVerb = 2
    Verb = 3
    Adjective = 4
    Number = 5
    Adverb = 6
    Pronoun = 7
    PronounAdjective = 8   #  ĉiuj, kia, etc.
    Preposition = 9
    Conjunction = 10
    Subjunction = 11
    Interjection = 12
    Prefix = 13
    TechPrefix = 14  # technical prefix,(hiper-, mega-) - not used independently
    Suffix = 15
    Article = 16
    Participle = 17
    Abbreviation = 18  # UEA, UNESKO
    Letter = 19

# Capitalization
class Cap(enum.Enum):
    Miniscule = 1    # butero
    Majuscule = 2    # Kanado
    AllCaps = 3        # UEA

# Transitivity - property of verbs
class Transitivity(enum.Enum):
    Transitive = 1
    Intransitive = 2    # Netransitiva
    Both = 3

# WithoutEnding
# This enumeration indicates whether a morpheme is a valid word
# without a grammatical ending.
# Eg: vi, tiu, ankaŭ, jes, pro, post
class WithoutEnding(enum.Enum):
    No = 1
    Yes = 2

# WithEnding
# This enumeration indicates whether a morpheme can accept a grammatical ending.
# Examples: hom-on, skrib-is, bon-e
class WithEnding(enum.Enum):
    No = 1
    Yes = 2

# Synthesis - Defines limits on morphology.
# Difinas kiel radikoj kuniĝas en morfologio.
class Synthesis(enum.Enum):
    Suffix = 1    # The morpheme acts like a suffix.
    Prefix = 2    # The morpheme acts like a prefix.
    Participle = 3    # The morpheme acts like a participle ending (-int, -it, etc.)
    Limited = 4       # Limited combinability.
    UnLimited = 5    # Unlimited (Ne Limigita).
    No = 6          # Does not combine.  (Ne)


# Meaning of dictionary entry.
class Meaning(enum.Enum):
    N = 1    # N means not defined.
    LEGOMO = 2
    BOATO = 3
    KRUSTULO = 4
    INSULO = 5
    RELIGIO = 6
    HERBO = 7
    KOLORO = 8
    PLANTO = 9
    FESTO = 10
    LIBRO = 11
    LOKO = 12
    DROGO = 13
    LAGO = 14
    PSEUXDOSCI = 15
    RELPOSTENO = 16
    PROFESIO = 17
    GRAMATIKO = 18
    EHXINODERMO = 19
    MEDIKAMENTO = 20
    REGIONO = 21
    BIOLOGIO = 22
    BIRDO = 23
    URBO = 24
    VETURILO = 25
    LANDO = 26
    ETNO = 27
    KANTO = 28
    VESTAJXO = 29
    TITOLO = 30
    REGANTO = 31
    RIVERO = 32
    ARTO = 33
    ERAO = 34
    PROVINCO = 35
    MUZIKO = 36
    PERSONO = 37
    SXTATO = 38
    MAMULO = 39
    FISXO = 49
    MEZURUNUO = 41
    FUNGO = 42
    KURACARTO = 43
    ARMILO = 44
    ALGO = 45
    KOELENTERO = 46
    NUKSO = 47
    MONTO = 48
    GEOGRAFIO = 49
    TEHXNOLOGIO = 50
    MONATO = 51
    ARKITEKTURO = 52
    INSULARO = 53
    METIO = 54
    ASTRONOMIO = 55
    KREDO = 56
    MOLUSKO = 57
    REPTILIO = 58
    TRINKAJXO = 59
    ANIMALO = 60
    INSEKTO = 61
    FRUKTO = 62
    ARBUSTO = 63
    ARAKNIDO = 64
    AVIADILO = 65
    SPORTO = 66
    ELEMENTO = 67
    ALOJO = 68
    RELPERSONO = 69
    RELPROFESIO = 70
    KEMIAJXO = 71
    FILOZOFIO = 72
    SXTOFO = 73
    POSTENO = 74
    PARENCO = 75
    KONSTRUAJXO = 76
    CEREALO = 77
    DANCO = 78
    TAGO = 79
    POEMO = 80
    SXIPO = 81
    LUDILO = 82
    POEZIO = 83
    CXAMBRO = 84
    MANGXAJXO = 85
    ASTRO = 86
    ILO = 87
    MIKROBO = 88
    LUDO = 89
    DEZERTO = 90
    MITBESTO = 91
    DRAMO = 92
    VETERO = 93
    ARBO = 94
    SCIENCO = 95
    ORNAMAJXO = 96
    VERMO = 97
    MINERALO = 98
    SPICO = 99
    MASXINO = 100
    KONTINENTO = 101
    PERIODO = 102
    LINGVO = 103
    MEZURILO = 104
    MARO = 105
    MONTARO = 106
    MITPERSONO = 107
    FONETIKO = 108
    MONERO = 109
    MATEMATIKO = 110
    RANGO = 111
    ANATOMIO = 112
    STUDO = 113
    OPTIKO = 114
    AMFIBIO = 115
    MALSANO = 116
    MUZIKILO = 117
    GEOMETRIO = 118


def is_person(meaning):
    """This function checks whether the given meaning represents a person.
    Params:
        meaning
    Return:
        True if person, False otherwise
    """
    if meaning == Meaning.PERSONO: return True
    if meaning == Meaning.PARENCO: return True
    if meaning == Meaning.ETNO: return True
    if meaning == Meaning.PROFESIO: return True
    if meaning == Meaning.RANGO: return True
    if meaning == Meaning.REGANTO: return True
    if meaning == Meaning.TITOLO: return True
    if meaning == Meaning.POSTENO: return True
    if meaning == Meaning.RELPOSTENO: return True
    if meaning == Meaning.RELPROFESIO: return True
    if meaning == Meaning.MITPERSONO: return True
    return False
# is_person()

def is_animal(meaning):
    """This function checks whether the given meaning represents an animal.
    Params:
        meaning
    Return:
        True if animal, False otherwise
    """
    if meaning == Meaning.ANIMALO: return True
    if meaning == Meaning.MAMULO: return True
    if meaning == Meaning.BIRDO: return True
    if meaning == Meaning.FISXO: return True
    if meaning == Meaning.REPTILIO: return True
    if meaning == Meaning.MITBESTO: return True
    if meaning == Meaning.INSEKTO: return True
    if meaning == Meaning.ARAKNIDO: return True
    if meaning == Meaning.MOLUSKO: return True
    if meaning == Meaning.AMFIBIO: return True
    return False
# is_animal()

class EspDictEntry:
    """This class represents a dictionary entry in the Esperanto spelling dictionary."""

    def get_transitivity(self, s):
        """Transitivity of verbs."""
        if s == 'T': return Transitivity.Transitive
        if s == 'X': return Transitivity.Both
        return Transitivity.Intransitive

    def get_synthesis(self, s):
        """Synthesis defines how morphemes combine.
        """
        if s == 'P': return Synthesis.Prefix
        if s == 'S': return Synthesis.Suffix
        if s == 'PRT': return Synthesis.Participle
        if s == 'LM': return Synthesis.Limited
        if s == 'NLM': return Synthesis.UnLimited
        return Synthesis.No

    def get_part_of_speech(self, s):
        """This function determines which part of speech (POS)
        the given string represents.
        """
        if s == 'SUBST': return POS.Substantive
        if s == 'SUBSTVERBO': return POS.SubstantiveVerb
        if s == 'VERBO': return POS.Verb
        if s == 'ADJ': return POS.Adjective
        if s == 'NUMERO': return POS.Number
        if s == 'ADVERBO': return POS.Adverb
        if s == 'PRONOMO': return POS.Pronoun
        if s == 'PRONOMADJ': return POS.PronounAdjective
        if s == 'PREPOZICIO': return POS.Preposition
        if s == 'KONJUNKCIO': return POS.Conjunction
        if s == 'SUBJUNKCIO': return POS.Subjunction
        if s == 'INTERJEKCIO': return POS.Interjection
        if s == 'PREFIKSO': return POS.Prefix
        if s == 'TEHXPREFIKSO': return POS.TechPrefix
        if s == 'SUFIKSO': return POS.Suffix
        if s == 'ARTIKOLO': return POS.Article
        if s == 'PARTICIPO': return POS.Participle
        if s == 'MALLONGIGO': return POS.Abbreviation
        if s == 'LITERO': return POS.Letter
        print("Whoa, there is a problem with Part of Speech.")
        sys.exit(0)

    def get_without_ending(self, s):
        """If the string s is 'SF' (Sen Finaĵo) the morpheme is a valid
        word without an ending.
        """
        if s == 'SF': return WithoutEnding.Yes
        return WithoutEnding.No

    def get_with_ending(self, s):
        """If the string s is 'KF' (Kun Finaĵo) the morpheme can accept
        a grammatical ending.
        """
        if s == 'KF': return WithEnding.Yes
        return WithEnding.No

    def get_capitalization(self, original_word):
        """There are 3 kinds of capitalization:
        simio -> Cap.Miniscule
        Kanado -> Cap.Majuscule
        UEA-> Cap.UEA
        """
        first_ch = 'a'
        second_ch = 'a'
        if (len(original_word) > 1):   # dictionary entries must be 2 or >
            first_ch = original_word[0]
            second_ch = original_word[1]
        first_upper = first_ch.isupper()
        second_upper = second_ch.isupper()
        if (first_upper and second_upper):
            return Cap.AllCaps
        elif (first_upper):
            return Cap.Majuscule
        else:
            return Cap.Miniscule

    def display(self):
        """Display key information about this entry."""
        print("-- {} {} {} {} {}".format(self.morpheme, self.part_of_speech, self.meaning,
                                                self.part_of_speech, self.synthesis))

    def __init__(self, data_array):
        """The parameter 'data_array' contains 9 dictionary parameters as strings.
        """
        morpheme = x_to_accent(data_array[0])
        self.morpheme = morpheme
        self.length = len(morpheme)
        self.capitalization = self.get_capitalization(morpheme)
        self.part_of_speech = self.get_part_of_speech(data_array[1])
        self.meaning = Meaning[data_array[2]]
        self.transitivity = self.get_transitivity(data_array[3])
        self.without_ending = self.get_without_ending(data_array[4])
        self.with_ending = self.get_with_ending(data_array[5])
        self.synthesis = self.get_synthesis(data_array[6])
        self.rarity = int(data_array[7])
        self.flag = data_array[8]

    @classmethod
    def new_separator(cls, separator):
        """This function creates an entry to define a 'separator', that is, a grammatical
        ending placed between morphemes to aid pronunciation. For example,
        'fingr.o.montr.i'; the 'o' is a separator. For the moment, a valid separator will
        be 'o', 'a' or 'e'.
        Params: separator string
        Return: dictionary entry for separator
        """
        if separator == "o": pos = "SUBST"
        elif separator == "a": pos = "ADJ"
        elif separator == "e": pos = "ADVERBO"
        else: return None

        data = [separator, pos, "N", "N", "N", "N", "N", 0, "separator"]
        return EspDictEntry(data)
