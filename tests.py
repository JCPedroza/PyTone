from main import *

# --------------------------------------
# ------------ TESTS -------------------
# --------------------------------------

## Variables for testing:
note1 = Note(440,    "A")
note2 = Note(466.16, "Bb")
note3 = Note(493.88, "B")
note4 = Note(523.25, "C")
note8 = Note(659.26, "E")
note10 = Note(739.99, "Gb")


# step_count() tests
# note note pool -> interval
def TESTS_step_count():
    assert the_process.step_count(note1, note2, et12_pool) == 1
    assert the_process.step_count(note1, note3, et12_pool) == 2
    assert the_process.step_count(note1, note4, et12_pool) == 3
    assert the_process.step_count(note1, note8, et12_pool) == 7
    assert the_process.step_count(note3, note1, et12_pool) == -2


# chord_check() tests
# chord, pool -> chordname
def TESTS_chord_check():
    assert chord_check(['Ab', 'C', 'Eb', 'G']            ) == "Abmaj7"
    assert chord_check(['Ab', 'C', 'Eb', 'G'],  et12_pool) == "Abmaj7"
    assert chord_check(['A', 'C', 'Eb', 'G'],   et12_pool) == "Amin7b5"
    assert chord_check(['Bb', 'Db', 'E', 'Ab'], et12_pool) == "Bbmin7b5"
    assert chord_check(['B', 'D', 'Gb', 'A'],   et12_pool) == "Bmin7"
    assert chord_check(['C', 'E', 'G', 'Bb'],   et12_pool) == "C7"
    assert chord_check(['Db', 'F', 'Ab', 'C'],  et12_pool) == "Dbmaj7"
    assert chord_check(['D', 'Gb', 'A', 'Db'],  et12_pool) == "Dmaj7"
    assert chord_check(['Eb', 'G', 'Bb', 'Db'], et12_pool) == "Eb7"
    assert chord_check(['E', 'G', 'B', 'D'],    et12_pool) == "Emin7"
    assert chord_check(['F', 'Ab', 'B', 'Eb'],  et12_pool) == "Fmin7b5"
    assert chord_check(['G', 'B', 'D', 'F'],    et12_pool) == "G7"
    assert chord_check(['Gb', 'A', 'Db', 'E'],  et12_pool) == "Gbmin7"
    assert chord_check(['C', 'Eb', 'G', 'B'],   et12_pool) == "Cminmaj7"
    assert chord_check(['C', 'Eb', 'Gb', 'A'],  et12_pool) == "Cdim7"
    assert chord_check(['C', 'E', 'Ab', 'B'],   et12_pool) == "Cmaj7#5"
    assert chord_check(["A"],                   et12_pool) == False
    assert chord_check([],                      []) ==        False
    assert chord_check(["4"],                  ["1", "2"]) == False


# scalize() tests
# note, formula, pool -> scale
def TESTS_scalize():
    assert scalize("C", formulas.majbebop              ) == ['C', 'D', 'E', 'F', 'G', 'Ab', 'A', 'B']
    assert scalize("C", formulas.dombebop              ) == ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B']
    assert scalize("C", formulas.majblues              ) == ['C', 'D', 'Eb', 'E', 'G', 'A']
    assert scalize("C", formulas.twosemitri            ) == ['C', 'Db', 'D', 'Gb', 'G', 'Ab']
    assert scalize("C", formulas.tritone               ) == ['C', 'Db', 'E', 'Gb', 'G', 'Bb']
    assert scalize("C", formulas.prometheus            ) == ['C', 'D', 'E', 'Gb', 'A', 'Bb']
    assert scalize("C",  formulas.augmented            ) == ['C', 'Eb', 'E', 'G', 'Ab', 'B']
    assert scalize("A",  formulas.minblues             ) == ['A', 'C', 'D', 'Eb', 'E', 'G']
    assert scalize("C",  formulas.pentmaj              ) == ['C', 'D', 'E', 'G', 'A']
    assert scalize("A",  formulas.pentmin              ) == ['A', 'C', 'D', 'E', 'G']
    assert scalize("E",  formulas.istrian              ) == ['E', 'F', 'G', 'Ab', 'Bb', 'B']
    assert scalize("C",  formulas.wholetone            ) == ["C", "D", "E", "Gb", "Ab", "Bb"]
    assert scalize("C",  formulas.ionian               ) == ["C", "D", "E", "F", "G", "A", "B"]
    assert scalize("C",  formulas.ionian,     et12_pool) == ["C", "D", "E", "F", "G", "A", "B"]
    assert scalize("F",  formulas.ionian,     et12_pool) == ["F", "G", "A", "Bb", "C", "D", "E"]
    assert scalize("G",  formulas.ionian,     et12_pool) == ["G", "A", "B", "C", "D", "E", "Gb"]
    assert scalize("Bb", formulas.ionian,     et12_pool) == ["Bb", "C", "D", "Eb", "F", "G", "A"]
    assert scalize("Bb", formulas.mixolydian, et12_pool) == ["Bb", "C", "D", "Eb", "F", "G", "Ab"]
    assert scalize("D",  formulas.lydian,     et12_pool) == ["D", "E", "Gb", "Ab", "A", "B", "Db"]
    assert scalize("E",  formulas.dorian,     et12_pool) == ['E', 'Gb', 'G', 'A', 'B', 'Db', 'D']
    assert scalize("B",  formulas.aeolian,    et12_pool) == ['B', 'Db', 'D', 'E', 'Gb', 'G', 'A']
    assert scalize("Db", formulas.phrygian,   et12_pool) == ['Db', 'D', 'E', 'Gb', 'Ab', 'A', 'B']
    assert scalize("Eb", formulas.locrian,    et12_pool) == ['Eb', 'E', 'Gb', 'Ab', 'A', 'B', 'Db']
    assert scalize("B",  [2, 2, 2, 2],                et12_pool) == ['B', 'Db', 'Eb', 'F']
    assert scalize("A",  formulas.melodicmin, et12_pool) == ['A', 'B', 'C', 'D', 'E', 'Gb', 'Ab']
    assert scalize("A",  formulas.harmmin,    et12_pool) == ['A', 'B', 'C', 'D', 'E', 'F', 'Ab']
    assert scalize("D",  formulas.dimhw,      et12_pool) == ['D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B', 'C']
    assert scalize("C",  formulas.dimwh,      et12_pool) == ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B']
    assert scalize("C",  formulas.altoct,     et12_pool) == ['C', 'Db', 'Eb', 'E', 'F', 'Gb', 'Ab', 'Bb']
    assert scalize("HH", formulas.locrian,    et12_pool) == False
    assert scalize("1",  [1, 1, 2],         ["1", "2"]) == ['1', '2', '1']
    assert scalize("1",  [1, 1],            ["1", "2"]) == ['1', '2']
    assert scalize("1",  [1, 1, 2, 2],      ["1", "2"]) == ['1', '2', '1', '1']
    assert scalize("",   [],                []) ==         False


# chordize() tests
# scale -> chordscale
def TESTS_chordize():
    assert chordize(scalize("G",  formulas.ionian                ), 2) == [['G', 'B', 'D', 'Gb'], ['A', 'C', 'E', 'G'], ['B', 'D', 'Gb', 'A'], ['C', 'E', 'G', 'B'], ['D', 'Gb', 'A', 'C'], ['E', 'G', 'B', 'D'], ['Gb', 'A', 'C', 'E']]
    assert chordize(scalize("G",  formulas.ionian,      et12_pool), 2) == [['G', 'B', 'D', 'Gb'], ['A', 'C', 'E', 'G'], ['B', 'D', 'Gb', 'A'], ['C', 'E', 'G', 'B'], ['D', 'Gb', 'A', 'C'], ['E', 'G', 'B', 'D'], ['Gb', 'A', 'C', 'E']]
    assert chordize(scalize("G",  formulas.ionian,      et12_pool), 1) == [['G', 'B', 'D'], ['A', 'C', 'E'], ['B', 'D', 'Gb'], ['C', 'E', 'G'], ['D', 'Gb', 'A'], ['E', 'G', 'B'], ['Gb', 'A', 'C']]
    assert chordize(scalize("C",  formulas.ionian,      et12_pool), 2) == [['C', 'E', 'G', 'B'], ['D', 'F', 'A', 'C'], ['E', 'G', 'B', 'D'], ['F', 'A', 'C', 'E'], ['G', 'B', 'D', 'F'], ['A', 'C', 'E', 'G'], ['B', 'D', 'F', 'A']]
    assert chordize(scalize("C",  formulas.aeolian,     et12_pool), 2) == [['C', 'Eb', 'G', 'Bb'], ['D', 'F', 'Ab', 'C'], ['Eb', 'G', 'Bb', 'D'], ['F', 'Ab', 'C', 'Eb'], ['G', 'Bb', 'D', 'F'], ['Ab', 'C', 'Eb', 'G'], ['Bb', 'D', 'F', 'Ab']]
    assert chordize(scalize("Bb", formulas.mixolydian,  et12_pool), 2) == [['Bb', 'D', 'F', 'Ab'], ['C', 'Eb', 'G', 'Bb'], ['D', 'F', 'Ab', 'C'], ['Eb', 'G', 'Bb', 'D'], ['F', 'Ab', 'C', 'Eb'], ['G', 'Bb', 'D', 'F'], ['Ab', 'C', 'Eb', 'G']]
    assert chordize(scalize("Bb", formulas.melodicmin,  et12_pool), 2) == [['Bb', 'Db', 'F', 'A'], ['C', 'Eb', 'G', 'Bb'], ['Db', 'F', 'A', 'C'], ['Eb', 'G', 'Bb', 'Db'], ['F', 'A', 'C', 'Eb'], ['G', 'Bb', 'Db', 'F'], ['A', 'C', 'Eb', 'G']]
    assert chordize(scalize("Bb", formulas.harmmin,     et12_pool), 2) == [['Bb', 'Db', 'F', 'A'], ['C', 'Eb', 'Gb', 'Bb'], ['Db', 'F', 'A', 'C'], ['Eb', 'Gb', 'Bb', 'Db'], ['F', 'A', 'C', 'Eb'], ['Gb', 'Bb', 'Db', 'F'], ['A', 'C', 'Eb', 'Gb']]
    assert chordize(scalize("A",  formulas.melodicmin,  et12_pool), 2) == [['A', 'C', 'E', 'Ab'], ['B', 'D', 'Gb', 'A'], ['C', 'E', 'Ab', 'B'], ['D', 'Gb', 'A', 'C'], ['E', 'Ab', 'B', 'D'], ['Gb', 'A', 'C', 'E'], ['Ab', 'B', 'D', 'Gb']]
    assert chordize(scalize("A",  formulas.harmmin,     et12_pool), 2) == [['A', 'C', 'E', 'Ab'], ['B', 'D', 'F', 'A'], ['C', 'E', 'Ab', 'B'], ['D', 'F', 'A', 'C'], ['E', 'Ab', 'B', 'D'], ['F', 'A', 'C', 'E'], ['Ab', 'B', 'D', 'F']]


# harmonize() tests
# chord -> harmony
def TESTS_harmonize():
    assert harmonize("C",  formulas.ionian                ) == ['Cmaj7', 'Dmin7', 'Emin7', 'Fmaj7', 'G7', 'Amin7', 'Bmin7b5']
    assert harmonize("C",  formulas.ionian,      et12_pool) == ['Cmaj7', 'Dmin7', 'Emin7', 'Fmaj7', 'G7', 'Amin7', 'Bmin7b5']
    assert harmonize("Bb", formulas.ionian,      et12_pool) == ['Bbmaj7', 'Cmin7', 'Dmin7', 'Ebmaj7', 'F7', 'Gmin7', 'Amin7b5']
    assert harmonize("G",  formulas.ionian,      et12_pool) == ['Gmaj7', 'Amin7', 'Bmin7', 'Cmaj7', 'D7', 'Emin7', 'Gbmin7b5']
    assert harmonize("E",  formulas.ionian,      et12_pool) == ['Emaj7', 'Gbmin7', 'Abmin7', 'Amaj7', 'B7', 'Dbmin7', 'Ebmin7b5']
    assert harmonize("A",  formulas.aeolian,     et12_pool) == ['Amin7', 'Bmin7b5', 'Cmaj7', 'Dmin7', 'Emin7', 'Fmaj7', 'G7']
    assert harmonize("Ab", formulas.aeolian,     et12_pool) == ['Abmin7', 'Bbmin7b5', 'Bmaj7', 'Dbmin7', 'Ebmin7', 'Emaj7', 'Gb7']
    assert harmonize("D",  formulas.aeolian,     et12_pool) == ['Dmin7', 'Emin7b5', 'Fmaj7', 'Gmin7', 'Amin7', 'Bbmaj7', 'C7']
    assert harmonize("D",  formulas.lydian,      et12_pool) == ['Dmaj7', 'E7', 'Gbmin7', 'Abmin7b5', 'Amaj7', 'Bmin7', 'Dbmin7']
    assert harmonize("Db", formulas.lydian,      et12_pool) == ['Dbmaj7', 'Eb7', 'Fmin7', 'Gmin7b5', 'Abmaj7', 'Bbmin7', 'Cmin7']
    assert harmonize("F",  formulas.lydian,      et12_pool) == ['Fmaj7', 'G7', 'Amin7', 'Bmin7b5', 'Cmaj7', 'Dmin7', 'Emin7']
    assert harmonize("Gb", formulas.mixolydian,  et12_pool) == ['Gb7', 'Abmin7', 'Bbmin7b5', 'Bmaj7', 'Dbmin7', 'Ebmin7', 'Emaj7']
    assert harmonize("B",  formulas.mixolydian,  et12_pool) == ['B7', 'Dbmin7', 'Ebmin7b5', 'Emaj7', 'Gbmin7', 'Abmin7', 'Amaj7']
    assert harmonize("C",  formulas.mixolydian,  et12_pool) == ['C7', 'Dmin7', 'Emin7b5', 'Fmaj7', 'Gmin7', 'Amin7', 'Bbmaj7']
    assert harmonize("A",  formulas.dorian,      et12_pool) == ['Amin7', 'Bmin7', 'Cmaj7', 'D7', 'Emin7', 'Gbmin7b5', 'Gmaj7']
    assert harmonize("Db", formulas.dorian,      et12_pool) == ['Dbmin7', 'Ebmin7', 'Emaj7', 'Gb7', 'Abmin7', 'Bbmin7b5', 'Bmaj7']
    assert harmonize("Ab", formulas.dorian,      et12_pool) == ['Abmin7', 'Bbmin7', 'Bmaj7', 'Db7', 'Ebmin7', 'Fmin7b5', 'Gbmaj7']
    assert harmonize("A",  formulas.phrygian,    et12_pool) == ['Amin7', 'Bbmaj7', 'C7', 'Dmin7', 'Emin7b5', 'Fmaj7', 'Gmin7']
    assert harmonize("C",  formulas.phrygian,    et12_pool) == ['Cmin7', 'Dbmaj7', 'Eb7', 'Fmin7', 'Gmin7b5', 'Abmaj7', 'Bbmin7']
    assert harmonize("Db", formulas.phrygian,    et12_pool) == ['Dbmin7', 'Dmaj7', 'E7', 'Gbmin7', 'Abmin7b5', 'Amaj7', 'Bmin7']
    assert harmonize("A",  formulas.locrian,     et12_pool) == ['Amin7b5', 'Bbmaj7', 'Cmin7', 'Dmin7', 'Ebmaj7', 'F7', 'Gmin7']
    assert harmonize("B",  formulas.locrian,     et12_pool) == ['Bmin7b5', 'Cmaj7', 'Dmin7', 'Emin7', 'Fmaj7', 'G7', 'Amin7']
    assert harmonize("E",  formulas.locrian,     et12_pool) == ['Emin7b5', 'Fmaj7', 'Gmin7', 'Amin7', 'Bbmaj7', 'C7', 'Dmin7']
    assert harmonize("A",  formulas.melodicmin,  et12_pool) == ['Aminmaj7', 'Bmin7', 'Cmaj7#5', 'D7', 'E7', 'Gbmin7b5', 'Abmin7b5']
    assert harmonize("A",  formulas.harmmin,     et12_pool) == ['Aminmaj7', 'Bmin7b5', 'Cmaj7#5', 'Dmin7', 'E7', 'Fmaj7', 'Abdim7']
    assert harmonize("C",  formulas.harmmin,     et12_pool) == ['Cminmaj7', 'Dmin7b5', 'Ebmaj7#5', 'Fmin7', 'G7', 'Abmaj7', 'Bdim7']
    assert harmonize("C",  formulas.melodicmin,  et12_pool) == ['Cminmaj7', 'Dmin7', 'Ebmaj7#5', 'F7', 'G7', 'Amin7b5', 'Bmin7b5']
    assert harmonize("E",  formulas.dimhw,       et12_pool) == ['Edim7', 'Fdim7', 'Gdim7', 'Abdim7', 'Bbdim7', 'Bdim7', 'Dbdim7', 'Ddim7']
    assert harmonize("B",  formulas.dimwh,       et12_pool) == ['Bdim7', 'Dbdim7', 'Ddim7', 'Edim7', 'Fdim7', 'Gdim7', 'Abdim7', 'Bbdim7']

# Run the tests:
TESTS_step_count()
TESTS_chord_check()
TESTS_scalize()
TESTS_chordize()
TESTS_harmonize()

print "All Tests Passed :D"
