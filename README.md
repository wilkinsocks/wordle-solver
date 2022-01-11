# Wordle Solver
*This is just for fun* 😭

[Wordle](https://www.powerlanguage.co.uk/wordle/) is a word guessing game.

You must guess 5 letters in 6 goes. After each go, Wordle reveals the following:
- 🟩 Letter is present in the word, and it's in the correct place!
- 🟨 Letter is present in the word, but it's in the wrong place.
- ⬛️ Letter is not in the word.

This CLI tool takes a guess, and provides possible answers.

## How to use
### Searching for patterns
`./scripts/search { SEARCH PATTERN }` — Searches dictionary for pattern

For the *search pattern*, use letters `A-Z` with `_` for blanks; e.g. `GU_G_`.

#### Making guesses:

`./scripts/search B_A_H`  

#### Response:
```
🔍 Found 4 possibilities for: [B _ A _ H]
----------------------------------------
BEACH
BEATH
BRACH
BRASH
```

#### Making guesses with missing letters:

`./scripts/search B_A_H --missing C D`  

#### Response:
```
🔍 Found 2 possibilities for: [B _ A _ H] without [C,D]
------------------------------------------------------
BEATH
BRASH
```

#### Making guesses including letters without placing:

`./scripts/search B_A_H --including C`  

#### Response:
```
🔍 Found 2 possibilities for: [B _ A _ H]
----------------------------------------
BEACH
BRACH
```

## Building
### Running in Docker:
`./scripts/bootstrap` — Starts required Docker containers

## Dictionary source
This tool uses Project Gutenberg: Webster's Unabridged Dictionary, However it's not committed to this repo.  
To obtain the source, download the plain text version at the following URL [Unabridged Dictionary Plain Text](https://www.gutenberg.org/ebooks/29765.txt.utf-8), and add the file to `./data/dictionary.txt`

Or use the following command: 
```
curl https://www.gutenberg.org/ebooks/29765.txt.utf-8 --output ./data/dictionary.txt
```
