from stats import get_count_words, get_characters_dictionary, sort_characters_dictionary_and_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    num_words = get_count_words(file_contents)
    characters_dictionary = get_characters_dictionary(file_contents)
    sorted_characters_dictionary = sort_characters_dictionary_and_count(characters_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count --------")
    for char in sorted_characters_dictionary:
        print(char)
    print("============= END ===============")

main()
