import sys
import re
import constants
from word_search import WordSearch

if len(sys.argv) < 2:
    print('No Wordle pattern passed')
    sys.exit()

pattern_input = sys.argv[1]

if len(pattern_input) != constants.WORDLE_LEGNTH:
    print(f'Wordle pattern should be {constants.WORDLE_LEGNTH} characters long')
    sys.exit()

pattern_input = pattern_input.upper()

letters = list(pattern_input)
letters_list = []

for letter in letters:
    if letter == '_':
        letters_list.append(False)
        continue

    pattern = re.compile('[A-Z]+')

    if not pattern.fullmatch(letter):
        print(f'{letter} is not allowed! You may only use A-z and _ for blanks')
        sys.exit()

    letters_list.append(letter)

search = WordSearch()
possibilities = search.search_possibilities(letters_list)

formatted_input = []

for letter in letters_list:
    if letter:
        formatted_input.append(letter)
    else:
        formatted_input.append('_')

formatted_input = ' '.join(formatted_input)

if len(possibilities) == 0:
    print(f'No results found for: {formatted_input}')
    sys.exit()

message = f'🔍 Found {len(possibilities)} possibilities for: {formatted_input}'

print(message)
print('-' * len(message))
print('')

for word in possibilities:
    print(word)
