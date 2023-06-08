from models.Word import Word
import string

# A class for a phrase that is formed of words using the english alphabet
class Phrase(Word):
    
    def __init__(self, words,seperator=" ",alphabet=string.ascii_letters):

        self.words = words
        self.phrase = ""
        for word in words:
            self.phrase += word.word + seperator
        self.word_count = len(self.words)

    def get_words(self):
        for w in self.words:
            yield w

    def __str__(self):
        return self.phrase

    def __repr__(self):
        return self.phrase

    def __eq__(self, other):
        return self.phrase == other.phrase

    def __len__(self):
        return self.word_count
    
    def to_bytes(self):
        return self.phrase.encode()