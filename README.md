# Random Name Generator

## Overview

The Random Name Generator is a Python script designed to generate random names by combining words from a given wordlist. By default, the script uses the 'EFF's Long Wordlist', which can be found at [https://www.eff.org/dice](https://www.eff.org/dice). This tool is useful for generating unique identifiers, character names for games or stories, or any other purpose where random, meaningful names are needed.

## Features

- Generate random names by combining a specified number of words.
- Uses 'EFF's Long Wordlist' by default, with support for both local JSON wordlists and remote wordlists via URLs.
- Customizable word count and dividing character in generated names.
- Includes a test wordlist for quick setup and testing.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library for Python (for handling remote wordlists)

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/pjburnhill/random-name-generator.git
cd random-name-generator
```

### Usage

Run the script with Python, optionally providing parameters for customization:

```bash
python random_name_generator.py [--num-words NUM_WORDS] [--dividing-character DIVIDING_CHARACTER] [--wordlist WORDLIST]
```

- `--num-words`: Number of words to use in the generated name (default: 3)
- `--dividing-character`: Character to use for dividing words in the name (default: '-')
- `--wordlist`: Path to a local JSON file or URL of the wordlist (default: EFF wordlist)

### Test Wordlist

The repository includes a test wordlist located at `data/words.json` for local testing. This JSON file contains a small list of words:

```
[
  "word1",
  "word2",
  "word3",
  "word4",
  "word5",
  "word6",
  "word7",
  "word8",
  "word9",
  "word10"
]
```

You can use this file by specifying `--wordlist data/words.json` when running the script.

## License

This project is open-source and available under the [MIT License](LICENSE).
