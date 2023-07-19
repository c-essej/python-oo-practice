from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        self.file = open(path)
        self.list = []


    def make_list(self):
        # self.list = self.file.readlines()
        self.list = [item.strip() for item in self.file.readlines()]

    def random(self):
        return choice(self.list)



