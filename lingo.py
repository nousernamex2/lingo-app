
import argparse
from spellchecker import SpellChecker

def correct_word(word, language):
    try:
        # Initialize spell checker with specified language
        spell = SpellChecker(language=language)

        # Correct the word
        return spell.correction(word)
    except Exception as e:
        return f"Error occurred while processing the word: {e}"

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Lingo: Correct words in English or German.')
    parser.add_argument('word', type=str, help='The word to correct')
    parser.add_argument('-d', '--german', action='store_true', help='Spellcheck in German')
    parser.add_argument('-e', '--english', action='store_true', help='Spellcheck in English')

    # Parse arguments
    args = parser.parse_args()

    # Determine the language for spell checking
    if args.german:
        language = 'de'
    elif args.english:
        language = 'en'
    else:
        raise ValueError("Please specify a language for spell checking (-d for German, -e for English)")

    # Correct the word
    result = correct_word(args.word, language)
    print(result)

if __name__ == "__main__":
    main()
