def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"------Begin report of {book_path}------\n\n")
    print(f"The book contains {num_words} words\n\n")
    create_report(chars_dict)
    print("\n\n------End Report------")
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def create_report(chars):
    dict_list = []
    for key, value in chars.items():
        dict_list.append({"char": key, "num": value})

    dict_list.sort(reverse=True, key=sort_on)

    for i in range(len(dict_list)):
        print(f"The {dict_list[i]["char"]} character was used {dict_list[i]["num"]} times")

def sort_on(dict):
    return dict["num"]


main()
