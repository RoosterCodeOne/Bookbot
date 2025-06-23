import sys
from stats import how_many_words, how_much_of_letter, separate_ind_dicts

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

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted_count:
        print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

main()