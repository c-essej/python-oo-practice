from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        self.file = open(path)


    def make_list(self):
        return self.file.readlines()

    def random(self):
        return choice(self.make_list())



