# Lingo - Spell Correction Tool

## Overview
`lingo` is a simple command-line application designed to provide quick and efficient spell correction. It supports both English and German languages, making it versatile for a wide range of users. With an easy-to-use command-line interface, `lingo` is an ideal tool for those who need fast and reliable spell checking.

## Features
- Spell correction in English and German.
- Command-line interface for ease of use.
- Fast and efficient processing of input words.

## Installation

Before you begin, ensure you have Python installed on your system. `lingo` is developed to work with Python 3.

### Dependencies
- `pyspellchecker`: Used for spell checking functionality.

To install the required library, run:

pip install pyspellchecker

### Setting Up

    Clone the repository or download the lingo.py script to your desired directory.

    Make the script executable (optional):

    bash

    chmod +x /path/to/lingo.py

### Adding as a Command-Line Tool

To use lingo directly from your terminal, you can set up an alias. Add the following line to your .bashrc, .bash_profile, or .zshrc:

bash

`alias lingo='python3 /path/to/lingo.py'`

Replace /path/to/lingo.py with the actual path to your script. After editing the file, apply the changes:

shell

`source ~/.bashrc`

or

zshrc

`source ~/.zshrc`

### Usage

To use lingo, run it from the terminal with the following syntax:

For English spell correction:

`lingo -e "word"`

For German spell correction:


`lingo -d "wort"`

Replace "word" or "wort" with the word you want to spell check.

### Contributing

Contributions to lingo are welcome! If you have suggestions for improvements or bug reports, please open an issue or a pull request.
