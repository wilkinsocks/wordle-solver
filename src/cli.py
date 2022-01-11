import sys
import re
import argparse
import constants
from word_search import WordSearch

def letter_valid(letter):
    pattern = re.compile('[A-Z]+')
    return pattern.fullmatch(letter)

args_parser = argparse.ArgumentParser()
args_parser.add_argument('guess')
args_parser.add_argument('--missing', nargs='+')
args = args_parser.parse_args()

pattern_input = args.guess
missing_letters = args.missing

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

    if not letter_valid(letter):
        print(f'{letter} is not allowed! You may only use A-Z and _ for blanks')
        sys.exit()

    letters_list.append(letter)

if missing_letters:
    for missing_letter in missing_letters:
        if missing_letter in letters:
            print(f'The letter {missing_letter} cannot be guessed and in the missing letters list')
            sys.exit()

search = WordSearch(missing_letters)

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

if len(possibilities) == 1:
    message = f'🔍 Found only 1 possibility for: [{formatted_input}]'
else:
    message = f'🔍 Found {len(possibilities)} possibilities for: [{formatted_input}]'

if missing_letters:
    formatted_missing_letters = ','.join(missing_letters)
    message += f' without [{formatted_missing_letters}]'

print(message)
print('-' * len(message))

for word in possibilities:
    print(word)
