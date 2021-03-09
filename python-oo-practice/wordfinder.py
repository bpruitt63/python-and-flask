"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    def __init__(self, file):
        self.words = []
        self.num_read = 0
        f = open(file)
        for word in f:
            self.words.append(word)
            self.num_read += 1
        f.close()
        print(f'{self.num_read} words read')

    def random(self):
        i = randint(0, self.num_read - 1)
        result = self.words[i]
        if result.endswith('\n'):
            result = result[0:-1]
        return result

class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)

    def random(self):
        result = WordFinder.random(self)
        if result.startswith('#') or result == '':
            result = SpecialWordFinder.random(self)
        return result