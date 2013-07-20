class Sound:
    def __init__(self, frequency, velocity=64, attack=0, decay=0, sustain=127, release=0):
        self.frequency = frequency
        self.velocity = velocity
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release

    def __str__(self):
        """ called when printing a Sound object, returns object's state """
        return ("Freq:" + str(self.frequency) + " Vel:" + str(self.velocity) +
                " Att:" + str(self.attack) + " Dec:" + str(self.decay) +
                " Sus:" + str(self.sustain) + " Rel:" + str(self.release))
