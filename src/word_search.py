import constants
import sys

class WordSearch():
    def __init__(self, included_letters=None, missing_letters=None):
        self.words = self.load_words()
        self.included_letters = included_letters
        self.missing_letters = missing_letters

    def search_possibilities(self, search_letters):
        possibilities = []

        for word in self.words:
            letters_in_word = list(word)

            if self.has_missing_letters(letters_in_word):
                continue
            
            if not self.has_included_letters(letters_in_word):
                continue

            if self.check_combination(letters_in_word, search_letters):
                possibilities.append(word)

        return possibilities

    def has_missing_letters(self, letters_in_word):
        if not self.missing_letters:
            return False

        for letter in letters_in_word:
            if letter in self.missing_letters:
                return True

        return False

    def has_included_letters(self, letters_in_word):
        if not self.included_letters:
            return True

        for letter in self.included_letters:
            if letter not in letters_in_word:
                return False

        return True

    def check_combination(self, letters_in_word, search_letters):
        for index, word_letter in enumerate(letters_in_word):
            search_letter = search_letters[index]
            
            if not search_letter:
                continue
            
            if search_letter != word_letter:
                return False

        return True

    def load_words(self):
        words = []

        with open(constants.OUTPUT_FILE) as file:
            for word in file:
                word = word.strip()

                if len(word) != constants.WORDLE_LEGNTH:
                    continue
            
                words.append(word)

        return words
