from stats import count_words, count_characters, sort_dictionary

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    frankenstein_text = get_book_text("books/frankenstein.txt")
    print(count_words(frankenstein_text))
    char_map = count_characters(frankenstein_text)
    print("--------- Character Count -------")
    sorted_dicts = sort_dictionary(char_map)
    for d in sorted_dicts:
        print(d["char"] + ": " + str(d["count"]))
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        read_data = f.read()
        return read_data

main()