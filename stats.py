from collections import defaultdict

def count_words(text):
    text_array = text.split()
    return f"Found {len(text_array)} total words"

def count_characters(text):
    char_map = defaultdict(int)
    text_array = text.split()
    for word in text_array:
        for c in word:
            c = c.lower()
            char_map[c] += 1
    return char_map

def sort_on(items):
    return items["count"]

def sort_dictionary(char_map):
    res = []
    for char, count in char_map.items():
        if char.isalpha():
            res.append({"char": char, "count": count})
    res.sort(reverse=True, key=sort_on)
    return res