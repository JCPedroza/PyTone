class Chord:
    def __init__(self, *notes):
        self.notes = notes

    def print_notes(self):
        """ print notes and their state """
        for e in self.notes:
            print e
