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
