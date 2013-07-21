# -*- coding: utf-8 -*-
# Start OOP: start with a formulas object! Instantiate it here (more formulas will be added, that will become big, soon!!!
# TO DO: scale_corrector(), harmonize() --needs to harmonize in other modes!-- , make comparisons between all possible notes in X parallel
# harmonies and all existing chords in a scenario (diatonic scenario, or diatonic 7ths, for example)
# apply systematic design
# !!!!!!! ANTES DE QUE CONTINUES CAMBIA TODO A OBJETOS O SERA MAS DIFICIL HACERLO MAS TARDE !!!

import formulas
import tests
from process import Process
from note import Note
from chord import Chord

# --------------------------------------
# -------- DATA DEFINITIONS ------------
# --------------------------------------

# note is : string
# interp: the name of a note

# chordname is: string
# interp: the name of a chord

# scale is: a list of: note
# interp: the notes that form a scale

# chord is: a list of: note
# interp: the notes that form a chord

# pool is: a list of note
# interp: all the possible note of an octave, in ascending order

# formula is: a list of int
# interp: the steps that define a mode (semitones, half-steps, etc)

# chordscale is: a list of: chord
# interp: chords that form a harmony

# harmony is: list of: chordname
# interp: chordnames of chords that form a harmony

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
# Process instance to provide note processing methods
the_process = Process()
