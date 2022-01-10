import constants

class WordSearch():
    def __init__(self):
        self.words = self.load_words()

    def search_possibilities(self, search_letters):
        possibilities = []

        for word in self.words:
            word_letters = list(word)

            is_possible = self.check_combination(word_letters, search_letters)

            if is_possible:
                possibilities.append(word)

        return possibilities

    def check_combination(self, word_letters, search_letters):
        for index, word_letter in enumerate(word_letters):
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
