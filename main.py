from stats import get_num_words
from stats import get_book_text
from stats import count_characters
import sys


def main():
    if len(sys.argv) <= 1:
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_count = count_characters(text)
    for item in character_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
