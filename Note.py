from Sound import Sound


class Note(Sound):
    def __init__(self, frequency, velocity=64, attack=0, decay=0, sustain=127, release=0, name="none"):
        Sound.__init__(self, frequency, velocity, attack, decay, sustain, release)
        self.name = name
