from stats import get_num_words
from stats import get_book_text
from stats import count_characters


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    character_count = count_characters(text)
    for item in character_count:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


main()
