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
et12_pool =       ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]
# the_modifiers is one of: possible chord quality
maj7_modifiers =     ["maj7", "min7", "7", "min7b5"]
all7th_modifiers =   ["maj7", "min7", "7", "min7b5", "dim7", "minmaj7", "maj7#5"]
# the_chords is one of: all possible (maj7, min7, 7, min7b5 for now) chords, using list comprehension
all_the_chords =  [a + b for a in et12_pool for b in all7th_modifiers]
# the_modes is one of: the modes (of major only for now)
the_modes =       ["lydian", "ionian", "mixolydian", "dorian", "aeolian", "phrygian", "locrian"]

# Formulas instance that provide formulas of scale structures:
formulas = formulas.Formulas()
# Process instance to provide note processing methods
the_process = Process()


# note, note, pool -> interval
# !!! everything, haz que regrese un objecto, las propiedades del objeto
# serán: diferencia de semitonos ascendente y descendente (entre ambas notas),
# su nombre corto, su nombre largo, y otras cosas que se te ocurran
def interval_check(note1, note2, pool=et12_pool):
    """ produces the interval between two notes in the given pool
        return false if the note is not found in the pool"""
    pass


# chord, pool -> chordname
# !!! more chord names, all triads, needs to recognizt altoct_formula harmony
def chord_check(chord, pool=et12_pool):
    """ returns the name of the chord as a string, returns False if no chord name is found """
    semitone_count = []
    chord_length = len(chord)
    pool_length = len(pool)
    for e in range(len(chord) - 1):
        next_one = chord[(e + 1) % chord_length]
        semitone_count.append(pool.index(chord[e]) - pool.index(next_one))
    # transforms semitone_count into abs numbers and corrects indexing dynamic issues
    for e in range(len(semitone_count)):
        if semitone_count[e] > 0:
            semitone_count[e] = semitone_count[e] - pool_length
    for e in range(len(semitone_count)):
        semitone_count[e] = abs(semitone_count[e])
    #debug print semitone_count
    # checks for patter, returns name
    if semitone_count ==   [3, 4, 3]:
        return str(chord[0]) + "min7"
    elif semitone_count == [4, 3, 4]:
        return str(chord[0]) + "maj7"
    elif semitone_count == [3, 3, 4]:
        return str(chord[0]) + "min7b5"
    elif semitone_count == [4, 3, 3]:
        return str(chord[0]) + "7"
    elif semitone_count == [3, 3, 3]:
        return str(chord[0]) + "dim7"
    elif semitone_count == [3, 4, 4]:
        return str(chord[0]) + "minmaj7"
    elif semitone_count == [4, 4, 3]:
        return str(chord[0]) + "maj7#5"
    else:
        # Returns False if no chord name is found
        return False


# scale -> scale
# !!! everything
def scale_corrector(scale, pool=et12_pool):
    """ returns a scale with no repeated note names if possible
        using a pool (list of notes) as reference"""
    pass


# note, formula, pool -> scale
def scalize(note, formula, pool=et12_pool):
    """ returns the scale of the given note in the given mode as a list
        pool is a list that contains all the possible semitones of the system's octave
        returns false if the note is not in the pool"""
    if note in pool:
        current_index = pool.index(note)
        return_list = []
        for e in formula:
            return_list.append(pool[current_index])
            current_index = (current_index + e) % len(pool)
        return return_list
    else:
        return False


# scale -> chordscale
def chordize(scale, depth):
    """ returns a list with the chords formed by thirds on a scale
        depth 1 = triads and depth 2 = 7th chords """
    chordscale = []
    scale_length = len(scale)
    if depth == 1:
        for e in range(len(scale)):
            chordscale.append([scale[e], scale[(e + 2) % scale_length], scale[(e + 4) % scale_length]])
    if depth == 2:
        for e in range(len(scale)):
            chordscale.append([scale[e], scale[(e + 2) % scale_length], scale[(e + 4) % scale_length], scale[(e + 6) % scale_length]])
    return chordscale


# chord -> harmony
def harmonize(note, formula=formulas.ionian, pool=et12_pool):
    """ returns harmony of a given note """
    chordscale = chordize(scalize(note, formula, pool), 2)
    harmony = []
    for e in chordscale:
        harmony.append(chord_check(e, pool))
    return harmony
