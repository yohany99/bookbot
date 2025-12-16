from stats import count_words, count_characters

def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    count_words(frankenstein_text)
    char_map = count_characters(frankenstein_text)
    print(char_map)

def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        read_data = f.read()
        return read_data

main()