from collections import defaultdict

def count_words(text):
    text_array = text.split()
    print(f"Found {len(text_array)} total words")

def count_characters(text):
    char_map = defaultdict(int)
    text_array = text.split()
    for word in text_array:
        for c in word:
            c = c.lower()
            char_map[c] += 1
    return char_map