import sys
import time
from stats import how_many_words, how_much_of_letter, separate_ind_dicts

def typewriter_effect(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
    return book_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_string = get_book_text(book_path)
    #print(book_string[:100])
    word_count = how_many_words(book_string)
    letter_count = how_much_of_letter(book_string)
    sorted_count = separate_ind_dicts(letter_count)

    typewriter_effect("============ BOOKBOT ============")
    typewriter_effect(f"Analyzing book found at {book_path}")
    typewriter_effect("----------- Word Count ----------")
    typewriter_effect(f"Found {word_count} total words")
    typewriter_effect("--------- Character Count -------")
    for pair in sorted_count:
        pair_string = (f"{pair["char"]}: {pair["num"]}")
        typewriter_effect(pair_string)

    print("============= END ===============")

main()