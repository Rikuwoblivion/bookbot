def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main(): 
    text= get_book_text("books/frankenstein.txt")
    print(get_num_words(text))
def get_num_words(text):
    text.split()
    return f"{len(text.split())} words found in the document"

def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def sort_on(item):
    return item["num"]

def sort_character_counts(char_counts):
    list1 = []
    for char, count in char_counts.items():
        if char.isalpha():
            list1.append({"char": char, "num": count})
    list1.sort(reverse=True, key=sort_on)
    return list1
