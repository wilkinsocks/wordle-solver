# Wordle Solver
*This is just for fun*
  

## Dictionary source
This tool uses Project Gutenberg: Webster's Unabridged Dictionary, However it's not committed to this repo.  
To obtain the source, download the plain text version at the following URL [Unabridged Dictionary Plain Text](https://www.gutenberg.org/ebooks/29765.txt.utf-8), and add the file to `./data/dictionary.txt`

Or use the following command:
```
curl https://www.gutenberg.org/ebooks/29765.txt.utf-8 --output ./data/dictionary.txt
```

  
## Reference
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

### Running in Docker:
`./scripts/bootstrap` — Starts required Docker containers
