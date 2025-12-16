from stats import count_words, count_characters, sort_dictionary
import sys

def main():
    try:
        text = get_book_text(sys.argv)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(count_words(text))
        char_map = count_characters(text)
        print("--------- Character Count -------")
        sorted_dicts = sort_dictionary(char_map)
        for d in sorted_dicts:
            print(d["char"] + ": " + str(d["count"]))
        print("============= END ===============")
    except Exception as e:
        print(e)
        return sys.exit(1)

def get_book_text(file_path):
    if len(file_path) < 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    else:
        with open(file_path[1], encoding="utf-8") as f:
            read_data = f.read()
            return read_data 

main()