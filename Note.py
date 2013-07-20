from Sound import Sound


class Note(Sound):
    def __init__(self, frequency, velocity=64, attack=0, decay=0, sustain=127,
                 release=0, name="none"):

        Sound.__init__(self, frequency, velocity, attack, decay, sustain, release)
        self.name = name

    def __str__(self):
        """ called when printing a Note object, returns object's state """
        return (" Name:" + self.name + " Freq:" + str(self.frequency) +
                " Vel:" + str(self.velocity) + " Att:" + str(self.attack) +
                " Dec:" + str(self.decay) + " Sus:" + str(self.sustain) +
                " Rel:" + str(self.release))
