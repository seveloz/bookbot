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

def get_num_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    lower_string = text.lower()
    totals = {}
    for c in lower_string:
        if c not in totals:
            totals[c] = 1
        else:
            totals[c] += 1
    dictionaries = [dict(char=key, num=value) for key, value in totals.items() if key.isalpha()]
    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries


def sort_on(dict):
    return dict["num"]


main()
