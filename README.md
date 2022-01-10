# Wordle Solver
*This is just for fun — WIP* 😭

[Wordle](https://www.powerlanguage.co.uk/wordle/) is a word guessing game.

You must guess 5 letters in 6 goes. After each go, Wordle reveals the following:
- 🟩 Letter is present in the word, and it's in the correct place!
- 🟨 Letter is present in the word, but it's in the wrong place.
- ⬛️ Letter is not in the word.

This CLI tool takes a guess, and provides possible answers.

## How to use
### Searching for patterns
`./scripts/search { SEARCH PATTERN }` — Searches dictionary for pattern  

#### Example:

`./scripts/search B_A__`  

#### Response:
```
🔍 Found 48 possibilities for: B _ A _ _
---------------------------------------

BEACH
BEADY
BEAMY
BEARD
BEARN
[..]
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
