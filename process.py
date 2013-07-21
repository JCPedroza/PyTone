class Process:

    # note, note, pool -> (int, int)
    # !!! do a version of this using frequency, code it using exceptions instead of False
    def step_count(self, note1, note2, pool):
        """ returns the distance between two notes in a pool"""
        if note1.name in pool and note2.name in pool:
            return pool.index(note2.name) - pool.index(note1.name)
        else:
            return False
