# -*- coding: utf-8 -*-
from note import Note
from chord import Chord

# et12_pool is: pool: "equal temperament 12 semitone pool" one of: 12 equal tempered notes
# Used as default pool
et12_pool = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]


# !!! do a version of this using frequency, code it using exceptions instead of False
# !!! doesn't worl poperly when comparing an element from the end of the pool with
# an element from the start of the pool, implement +len(pool) lke in the java version
def step_count(note1, note2, pool=et12_pool):
    """ note, note, pool -> int
    returns the distance between two notes in a pool """
    if note1.name in pool and note2.name in pool:
        return pool.index(note2.name) - pool.index(note1.name)
    else:
        return False


# !!! Type check for every argument, use exceptions
# !!! Use exeptions instead of false
def scalize(note, formula, pool=et12_pool):
    """ note (string or object), formula, pool -> scale
    returns the scale derived from the formula applied to the pool
    with note as root, accepts string or Note object"""
    if isinstance(note, Note):
        return _scalize_obj(note, formula, pool)
    elif type(note) == str:
        return _scalize_str(note, formula, pool)


def _scalize_obj(note, formula, pool):
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


def _scalize_str(note, formula, pool):
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
def chordize(scale, depth):
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


# chord -> harmony, !!! as in jatone this should be renamed !!! it needs chord namer to work!
# def harmonize(note, formula, pool=et12_pool):
#     """ returns harmony of a given note """
#     chordscale = chordize(scalize(note, formula, pool), 2)
#     harmony = []
#     for e in chordscale:
#         harmony.append(chord_check(e, pool))
#     return harmony


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

#===================================================================
#   Chord recognition
#   Algorithm taken from Music theory Python package, chords module (Copyright (C) 2008-2009, Bart Spaans)
#   Project page: https://code.google.com/p/mingus/
#===================================================================

def determine(chord, shorthand = False, no_inversions = False, no_polychords = False):
    """Names a chord. Can determine almost every chord, from a simple triad to a fourteen note polychord."""
    if chord == []:
        return []
    elif len(chord) == 1:
        return chord
    elif len(chord) == 2:
        return [intervals.determine(chord[0], chord[1])]
    elif len(chord) == 3:
        return determine_triad(chord, shorthand, no_inversions, no_polychords)
    elif len(chord) == 4:
        return determine_seventh(chord, shorthand, no_inversions, no_polychords)
    elif len(chord) == 5:
        return determine_extended_chord5(chord, shorthand, no_inversions, no_polychords)
    elif len(chord) == 6:
        return determine_extended_chord6(chord, shorthand, no_inversions, no_polychords)
    elif len(chord) == 7:
        return determine_extended_chord7(chord, shorthand, no_inversions, no_polychords)
    else:
        return determine_polychords(chord, shorthand)



def determine_triad(triad, shorthand = False, no_inversions = False, placeholder = None):
    """Names the triad. Returns answers in a list. The third argument should \
not be given. If shorthand is True the answers will be in abbreviated form.

Can determine major, minor, diminished and suspended triads. \
Also knows about invertions.

Examples:
{{{
>>> determine_triad(["A", "C", "E"])
'A minor triad'
>>> determine_triad(["C", "E", "A"])
'A minor triad, first inversion'
>>> determine_triad(["A", "C", "E"], True)
'Am'
}}}"""

    if len(triad) != 3:
        #warning: raise exception: not a triad
        return False

    def inversion_exhauster(triad, shorthand, tries, result):
        """Recursive helper function that runs tries every inversion
        and saves the result."""

        intval1 = intervals.determine(triad[0], triad[1], True)
        intval2 = intervals.determine(triad[0], triad[2], True)

        def add_result(short):
            result.append((short, tries, triad[0]))

        intval = intval1 + intval2
        if intval == "25": add_result("sus2")

        elif intval == "3b7": add_result("dom7") # changed from just '7'
        elif intval == "3b5": add_result("7b5") # why not b5?
        elif intval == "35": add_result("M")
        elif intval == "3#5": add_result("aug")
        elif intval == "36": add_result("M6")
        elif intval == "37": add_result("M7")

        elif intval == "b3b5": add_result("dim")
        elif intval == "b35": add_result("m")
        elif intval == "b36": add_result("m6")
        elif intval == "b3b7": add_result("m7")
        elif intval == "b37": add_result("m/M7")

        elif intval == "45": add_result("sus4")

        elif intval == "5b7": add_result("m7")
        elif intval == "57": add_result("M7")

        if tries != 3 and not no_inversions:
            return inversion_exhauster([triad[-1]] + triad[:-1], shorthand,\
                    tries + 1, result)
        else:
            res = []
            for r in result:
                if shorthand:
                    res.append(r[2] + r[0])
                else:
                    res.append(r[2] + chord_shorthand_meaning[r[0]] + int_desc(r[1]))

            return res

    return inversion_exhauster(triad, shorthand, 1, [])


def determine_seventh(seventh, shorthand = False, no_inversion = False, no_polychords = False):
    """Determines the type of seventh chord. Returns the results in a \
lists, ordered on inversions. Expects `seventh` to be a \
list of 4 notes. If `shorthand` is set to True, results \
will be returned in chord shorthand ('Cmin7', etc.) - inversions will be \
dropped in that case.
    Example:
{{{
>>> determine_seventh(['C', 'E', 'G', 'B'])
['C major seventh']
}}}"""

    if len(seventh) != 4:
        #warning raise exception: seventh chord is not a seventh chord
        return False

    def inversion_exhauster(seventh, shorthand, tries, result, polychords):
        """determine sevenths recursive functions"""

        # Check whether the first three notes of seventh
        # are part of some triad.
        triads = determine_triad(seventh[:3], True, True)

        # Get the interval between the first and last note
        intval3 = intervals.determine(seventh[0], seventh[3])

        def add_result(short, poly = False):
            """helper function"""
            result.append((short, tries, seventh[0], poly))

        # Recognizing polychords
        if tries == 1 and not no_polychords:
            polychords = polychords +  determine_polychords(seventh, shorthand)

        # Recognizing sevenths
        for triad in triads:
            # Basic triads
            triad = triad[len(seventh[0]):]
            if triad == "m":
                if intval3 == "minor seventh":
                    add_result("m7")
                elif intval3 == "major seventh":
                    add_result("m/M7")
                elif intval3 == "major sixth":
                    add_result("m6")
            elif triad == "M":
                if intval3 == "major seventh":
                    add_result("M7")
                elif intval3 == "minor seventh":
                    add_result("7")
                elif intval3 == "major sixth":
                    add_result("M6")
            elif triad == "dim":
                if intval3 == "minor seventh":
                    add_result("m7b5")
                elif intval3 == "diminished seventh":
                    add_result("dim7")
            elif triad == "aug":
                if intval3 == "minor seventh":
                    add_result("m7+")
                if intval3 == "major seventh":
                    add_result("M7+")
            elif triad == "sus4":
                if intval3 == "minor seventh":
                    add_result("sus47")
                elif intval3 == "minor second":
                    add_result("sus4b9")
            # Other
            elif triad == 'm7':
                if intval3 == 'perfect fourth':
                    add_result("11")
            elif triad == '7b5':
                if intval3 == 'minor seventh':
                    add_result("7b5")


        # Loop until we have exhausted all the inversions
        if tries != 4 and not no_inversion:
            return inversion_exhauster([seventh[-1]] + seventh[:-1], \
                            shorthand, tries + 1, result, polychords)
        else:
            # Return results
            res = []
            # Reset seventh
            seventh = [seventh[3]] + seventh[0:3]
            for x in result:
                if shorthand:
                    res.append(x[2] + x[0])
                else:
                    res.append(x[2] + chord_shorthand_meaning[x[0]] + int_desc(x[1]))
            return res + polychords
    return inversion_exhauster(seventh, shorthand, 1, [], [])


def determine_extended_chord5(chord, shorthand = False, no_inversions = False, no_polychords = False):
    """Determines the names of an extended chord"""
    if len(chord) != 5:
        #warning raise exeption: not an extended chord
        return False

    def inversion_exhauster(chord, shorthand, tries, result, polychords):
        """Recursive helper function"""

        def add_result(short):
            result.append((short, tries, chord[0]))

        triads = determine_triad(chord[:3], True, True)
        sevenths = determine_seventh(chord[:4], True, True, True)

        # Determine polychords
        if tries == 1 and not no_polychords:
            polychords += determine_polychords(chord, shorthand)


        # Determine 'normal' chords
        intval4 = intervals.determine(chord[0], chord[4])
        for seventh in sevenths:
            seventh = seventh[len(chord[0]):]
            if seventh == "M7":
                if intval4 == 'major second':
                    add_result("M9")
            elif seventh == "m7":
                if intval4 == 'major second':
                    add_result("m9")
                elif intval4 == 'perfect fourth':
                    add_result("m11")
            elif seventh == "7":
                if intval4 == 'major second':
                    add_result("9")
                elif intval4 == 'minor second':
                    add_result("7b9")
                elif intval4 == 'augmented second':
                    add_result("7#9")
                elif intval4 == 'minor third':
                    add_result("7b12")
                elif intval4 == 'augmented fourth':
                    add_result("7#11")
                elif intval4 == 'major sixth':
                    add_result("13")
            elif seventh == "M6":
                if intval4 == "major second":
                    add_result("6/9")
                elif intval4 == "minor seventh":
                    add_result("6/7")

        if tries != 5 and not no_inversions:
            return inversion_exhauster([chord[-1]] + chord[:-1], \
                        shorthand, tries + 1, result, polychords)
        else:
            res = []
            for r in result:
                if shorthand:
                    res.append(r[2] + r[0])
                else:
                    res.append(r[2] + chord_shorthand_meaning[r[0]] + int_desc(r[1]))
            return res + polychords

    return inversion_exhauster(chord, shorthand, 1, [], [])



def determine_extended_chord6(chord, shorthand = False, no_inversions = False, no_polychords = False):
    """Determines the names of an 6 note chord"""
    if len(chord) != 6:
        #warning raise exeption: not an extended chord
        return False

    def inversion_exhauster(chord, shorthand, tries, result, polychords):
        """Recursive helper function"""

        # Determine polychords
        if tries == 1 and not no_polychords:
            polychords += determine_polychords(chord, shorthand)

        def add_result(short):
            result.append((short, tries, chord[0]))

        ch = determine_extended_chord5(chord[:5], True, True, True)
        intval5 = intervals.determine(chord[0], chord[5])

        for c in ch:
            c = c[len(chord[0]):]
            if c == '9':
                if intval5 == 'perfect fourth':
                    add_result('11')
                elif intval5 == 'augmented fourth':
                    add_result('7#11')
                elif intval5 == 'major sixth':
                    add_result('13')
            elif c == 'm9':
                if intval5 == 'perfect fourth':
                    add_result('m11')
                elif intval5 == 'major sixth':
                    add_result('m13')
            elif c == 'M9':
                if intval5 == 'perfect fourth':
                    add_result('M11')
                elif intval5 == 'major sixth':
                    add_result('M13')

        if tries != 6 and not no_inversions:
            return inversion_exhauster([chord[-1]] + chord[:-1], \
                        shorthand, tries + 1, result, polychords)
        else:
            res = []
            for r in result:
                if shorthand:
                    res.append(r[2] + r[0])
                else:
                    res.append(r[2] + chord_shorthand_meaning[r[0]] + int_desc(r[1]))
            return res + polychords

    return inversion_exhauster(chord, shorthand, 1, [], [])


def determine_extended_chord7(chord, shorthand=False, no_inversions=False, no_polychords=False):
    """Determines the names of an 7 note chord"""
    if len(chord) != 7:
        #warning raise exeption: not an extended chord
        return False

    def inversion_exhauster(chord, shorthand, tries, result, polychords):
        """Recursive helper function"""

        # Determine polychords
        if tries == 1 and not no_polychords:
            polychords += determine_polychords(chord, shorthand)

        def add_result(short):
            result.append((short, tries, chord[0]))

        ch = determine_extended_chord6(chord[:6], True, True, True)
        intval6 = intervals.determine(chord[0], chord[6])

        for c in ch:
            c = c[len(chord[0]):]
            if c == '11':
                if intval6 == 'major sixth':
                    add_result('13')
            elif c == 'm11':
                if intval6 == 'major sixth':
                    add_result('m13')
            elif c == 'M11':
                if intval6 == 'major sixth':
                    add_result('M13')
                

        if tries != 6:
            return inversion_exhauster([chord[-1]] + chord[:-1], \
                        shorthand, tries + 1, result, polychords)
        else:
            res = []
            for r in result:
                if shorthand:
                    res.append(r[2] + r[0])
                else:
                    res.append(r[2] + chord_shorthand_meaning[r[0]] + int_desc(r[1]))
            return res + polychords

    return inversion_exhauster(chord, shorthand, 1, [], [])




def int_desc(tries):
    """Helper function that returns the inversion of the triad in a string"""
    if tries == 1:
        return ""
    elif tries == 2:
        return ", first inversion"
    elif tries == 3:
        return ", second inversion"
    elif tries == 4:
        return ", third inversion"


def determine_polychords(chord, shorthand = False):
    """Determines the polychords in chord. Can handle anything from polychords based on two triads to 6 note extended chords."""
    polychords = []

    function_list = [
            determine_triad, determine_seventh,
            determine_extended_chord5, determine_extended_chord6,
            determine_extended_chord7
            ]

    # Range tracking.
    if len(chord) <= 3:
        return []
    elif len(chord) > 14:
        return []
    elif len(chord) - 3 <= 5:
        function_nr = range(0, len(chord) - 3)
    else:
        function_nr = range(0, 5)

    for f in function_nr:
        for f2 in function_nr:
            # The clever part:
            # Try the function_list[f] on the len(chord) - (3 + f)
            # last notes of the chord. Then try the function_list[f2]
            # on the f2 + 3 first notes of the chord. Thus, trying
            # all possible combinations.
            for chord1 in function_list[f](chord[len(chord) -\
                (3 + f):], True, True, True):
                    for chord2 in function_list[f2](chord[:f2+3], \
                        True, True, True):
                        polychords.append("%s|%s" % (chord1, chord2))

    if shorthand:
        for p in polychords:
            p = p + " polychord"

    return polychords
