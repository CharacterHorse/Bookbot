import sys
from stats import get_num_words, get_num_letters, get_sorted_letter_dict


def get_book_text(filepath):
    with open(filepath) as file:
        content = file.read()
        print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}
----------- Word Count ----------
Found {get_num_words(content)} total words
--------- Character Count -------""")
        for item in get_sorted_letter_dict(get_num_letters(content)):
            print(f"{item['char']}: {item['num']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    get_book_text(filepath=sys.argv[1])


main()
