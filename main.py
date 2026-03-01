<<<<<<< HEAD
from stats import get_num_words, get_chars_dict, get_sorted_chars_list
=======
from stats import get_num_words, get_chars_dict, sorted_dict
>>>>>>> 7fff7b9 (jic)


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
<<<<<<< HEAD
    sorted_chars = get_sorted_chars_list(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(str(char))

=======
    sorted_dick = sorted_dict(chars_dict).sort
    print(f"Found {num_words} total words")
    print(chars_dict)
    print(sorted_dick)
>>>>>>> 7fff7b9 (jic)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
