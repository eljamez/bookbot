import sys

from stats import get_num_words
from stats import get_num_characters
from stats import get_chars_sorted

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = get_book_text(sys.argv[1])
    book_word_count = get_num_words(book)
    book_char_count = get_num_characters(book)
    book_sorted_chars = get_chars_sorted(book_char_count)
    response = f"{book_word_count} words found in the document"
    print(response)
    print(book_char_count)
    print("============ BOOKBOT ============")
    analyze_response = f"Analyzing book found at {sys.argv[1]}..."
    print(analyze_response)
    print("----------- Word Count ----------")
    total = f"Found {book_word_count} total words"
    print(total)
    print("--------- Character Count -------")
    for item in book_sorted_chars:
        if item["char"].isalpha():
            letter_count = f"{item["char"]}: {item["num"]}"
            print(letter_count)
    print("============ END ===============")

main()
