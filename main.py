def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    input_dict = get_chars_dict(text)
    sorted_c_dict = sort_on(input_dict)
    listed_items = list(sorted_c_dict.items())

    print(f"--- Begin report of {book_path} ---") 
    print(f"{num_words} words found in the document")
    for i in range(0,len(listed_items),2):
        char_1,count_1 = listed_items[i]
        print(f"The '{char_1}' character was found {count_1} times")
    print(f"--- End report ---")


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

def sort_on(data):
    return dict(sorted(data.items(), key = lambda item: item[1], reverse=True))

main()
