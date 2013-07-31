# -*- coding: utf-8 -*-

import formulas
import tests
from note import Note
from chord import Chord

# --------------------------------------
# ------------ Program -----------------
# --------------------------------------

# et12_pool is: pool: "equal temperament 12 semitone pool" one of: 12 equal tempered notes
et12_pool = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]
# the_modifiers is one of: possible chord quality
maj7_modifiers = ["maj7", "min7", "7", "min7b5"]
all7th_modifiers = ["maj7", "min7", "7", "min7b5", "dim7", "minmaj7", "maj7#5"]
# the_chords is one of: all possible (maj7, min7, 7, min7b5 for now) chords, using list comprehension
all_the_chords = [a + b for a in et12_pool for b in all7th_modifiers]
# the_modes is one of: the modes (of major only for now)
the_modes = ["lydian", "ionian", "mixolydian", "dorian", "aeolian", "phrygian", "locrian"]

# Formulas instance that provide formulas of scale structures:
formulas = formulas.Formulas()
