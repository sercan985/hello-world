import string

# A class for a word that is formed using the english alphabet
class Word:
    
    def __init__(self,word_letter_indexes,alphabet=string.ascii_letters):
        self.alphabet = alphabet
        self.word_letter_indexes = word_letter_indexes
        self.word = ""
        for index in word_letter_indexes:
            self.word += alphabet[index]

    def __str__(self):
        return self.word

    def __repr__(self):
        return self.word

    def __eq__(self, other):
        return self.word == other.word
    
    def __len__(self):
        return len(self.word)
    
    def to_bytes(self):
        return self.word.encode()