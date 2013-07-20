class Sound:
    def __init__(self, frequency, velocity=64, attack=0, decay=0, sustain=127, release=0):
        self.frequency = frequency
        self.velocity = velocity
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release
