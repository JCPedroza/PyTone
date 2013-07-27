# -*- coding: utf-8 -*-
from note import Note
from chord import Chord


class Process:

    # et12_pool is: pool: "equal temperament 12 semitone pool" one of: 12 equal tempered notes
    # Used as default pool
    et12_pool = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]

    # !!! do a version of this using frequency, code it using exceptions instead of False
    # !!! doesn't worl poperly when comparing an element from the end of the pool with
    # an element from the start of the pool, implement +len(pool) lke in the java version
    def step_count(self, note1, note2, pool=et12_pool):
        """ note, note, pool -> int
        returns the distance between two notes in a pool """
        if note1.name in pool and note2.name in pool:
            return pool.index(note2.name) - pool.index(note1.name)
        else:
            return False

    # !!! Type check for every argument, use exceptions
    # !!! Use exeptions instead of false
    def scalize(self, note, formula, pool=et12_pool):
        """ note (string or object), formula, pool -> scale
        returns the scale derived from the formula applied to the pool
        with note as root, accepts string or Note object"""
        if isinstance(note, Note):
            return self._scalize_obj(note, formula, pool)
        elif type(note) == str:
            return self._scalize_str(note, formula, pool)

    def _scalize_obj(self, note, formula, pool):
        """ helper for scalize, deals with Note objects """
        if note.name in pool:
            current_index = pool.index(note.name)
            return_list = []
            for e in formula:
                return_list.append(pool[current_index])
                current_index = (current_index + e) % len(pool)
            return return_list
        else:
            return False

    def _scalize_str(self, note, formula, pool):
        """ helper for scalize, deals with strings """
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
    # !!! consume and produce objects maybe?, as in jytone, this should be named harmonize
    def chordize(self, scale, depth):
        """ returns a list with the chords formed by thirds on a scale
            depth 1 = triads and depth 2 = 7th chords """
        chordscale = []
        scale_length = len(scale)
        if depth == 1:
            for e in range(scale_length):
                chordscale.append([scale[e], scale[(e + 2) % scale_length], scale[(e + 4) % scale_length]])
        if depth == 2:
            for e in range(scale_length):
                chordscale.append([scale[e], scale[(e + 2) % scale_length], scale[(e + 4) % scale_length], scale[(e + 6) % scale_length]])
        return chordscale

    # chord -> harmony, !!! as in jatone this should be renamed 
  
    def harmonize(self, note, formula, pool=et12_pool):
        """ returns harmony of a given note """
        chordscale = self.chordize(self.scalize(note, formula, pool), 2)
        harmony = []
        for e in chordscale:
            harmony.append(self.chord_check(e, pool))
        return harmony

    # !!! more chord names, all triads, needs to recognizt altoct_formula harmony
    # !!! use exceptions instead of false
    # !!! consume and poduce objects if needed: for now it can consume chord both as a list or as an object
    def chord_check(self, chord, pool=et12_pool):
        """ chord, pool -> chordname (string)
        returns the name of the chord as a string, returns False if no chord name is found """
        semitone_count = []
        if isinstance(chord, Chord):
            note_list = [e.name for e in chord.notes]
        elif type(chord) == list:
            note_list = chord
        chord_length = len(note_list)
        pool_length = len(pool)
        for e in range(len(note_list) - 1):
            next_one = note_list[(e + 1) % chord_length]
            semitone_count.append(pool.index(note_list[e]) - pool.index(next_one))
        # transforms semitone_count into abs numbers and corrects indexing dynamic issues
        for e in range(len(semitone_count)):
            if semitone_count[e] > 0:
                semitone_count[e] = semitone_count[e] - pool_length
        for e in range(len(semitone_count)):
            semitone_count[e] = abs(semitone_count[e])
        #debug print semitone_count
        # checks for patter, returns name
        if semitone_count == [3, 4, 3]:
            return str(note_list[0]) + "min7"
        elif semitone_count == [4, 3, 4]:
            return str(note_list[0]) + "maj7"
        elif semitone_count == [3, 3, 4]:
            return str(note_list[0]) + "min7b5"
        elif semitone_count == [4, 3, 3]:
            return str(note_list[0]) + "7"
        elif semitone_count == [3, 3, 3]:
            return str(note_list[0]) + "dim7"
        elif semitone_count == [3, 4, 4]:
            return str(note_list[0]) + "minmaj7"
        elif semitone_count == [4, 4, 3]:
            return str(note_list[0]) + "maj7#5"
        else:
            # Returns False if no chord name is found
            return False

    # scale -> scale
    # !!! everything
    def scale_corrector(scale, pool=et12_pool):
        """ returns a scale with no repeated note names if possible
            using a pool (list of notes) as reference"""
        pass

    # note, note, pool -> interval
    # !!! everything, haz que regrese un objecto, las propiedades del objeto
    # serán: diferencia de semitonos ascendente y descendente (entre ambas notas),
    # su nombre corto, su nombre largo, y otras cosas que se te ocurran
    def interval_check(note1, note2, pool=et12_pool):
        """ produces the interval between two notes in the given pool
            return false if the note is not found in the pool"""
        pass
