import re
import constants

def is_line_word(line):
    pattern = re.compile('[A-Z]+')
    return pattern.fullmatch(line)

def is_wordle_len(word):
    return len(word) == constants.WORDLE_LEGNTH

def process_data(data_file):
    with open(data_file) as file:
        for line in file:
            line = line.strip()

            if not is_line_word(line):
                continue

            word = line

            if not is_wordle_len(word):
                continue

            if word not in words:
                words[word] = None

words = {}
        
process_data(constants.INPUT_FILE)

with open(constants.OUTPUT_FILE, 'w') as file:
    for word in words:
        file.write(f'{ word }\n') 
