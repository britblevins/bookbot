import sys
from stats import get_word_num, get_char_num, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  

    number_of_words = get_word_num(get_book_text(sys.argv[1]))
    number_of_chars = get_char_num(get_book_text(sys.argv[1]))
    sorted_dict = sort_dict(number_of_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for dictionary in sorted_dict:
        for key in dictionary:
            print(f"{key}: {dictionary[key]}")

    print("============= END ===============")

main()