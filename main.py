import sys

from stats import character_count, get_book_text, sort_dict, words_in_book

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book = sys.argv[1]  # Takes the second arg in list, as a path to a book
    wordcount = words_in_book(book)
    # char_count = character_count(book)
    character_dict = sort_dict(book)
    print(f"Analyzing book found at {book}")
    print("---------------- Word Count --------------")
    print(f"Found {wordcount} total words")
    print("--------------Character Count -------------------")
    for d in character_dict:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")


main()
