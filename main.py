from stats import *
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()

    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_txt = get_book_text(sys.argv[1])

    num_words = count_words(book_txt)

    chars_dct = count_chars(book_txt)

    sorted_chars_dct = sort_dict(chars_dct)  #sorted by value (greatest to least)

    print("============ BOOKBOT ============")

    print(f'Analyzing book found at {sys.argv[1]}') 
    print("----------- Word Count ----------")


    print(f'Found {num_words} total words')

    print("--------- Character Count -------")

    for element in sorted_chars_dct:   #printing only alphabetical characters
        if element[0].isalpha():
            print(f'{element}')

        
    print("============= END ===============")

main()