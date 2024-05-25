# your code goes here!
class Anagram():
    def __init__(self, arg_word):
        self.word = sorted(arg_word.lower())

    def match(self, sample):
        return [w for w in sample if sorted(w.lower()) == self.word]
