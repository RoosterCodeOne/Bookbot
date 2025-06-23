def how_many_words(book_string):
    words = book_string.split()
    word_count = len(words)
    return word_count

def how_much_of_letter(book_string):
    letter_count = {}
    for letter in book_string:
        lowercase = letter.lower()
        if lowercase not in letter_count:
            letter_count[lowercase] = 1           
        else:
            letter_count[lowercase] += 1
    return letter_count

def sort_on(letter_dict):
    return letter_dict["num"]

def separate_ind_dicts(letter_dict):
    sorted = []
    for char, count in letter_dict.items():
        if char.isalpha():
            sorted.append({"char": char, "num": count})
    sorted.sort(reverse=True, key=sort_on)
    return sorted