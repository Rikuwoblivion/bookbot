from stats import get_num_words
from stats import get_char_count 
from stats import sort_character_counts
from stats import get_book_text
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============") 
    book_path = sys.argv[1]               # get the path from CLI
    text = get_book_text(book_path)       # pass it into the function

    print(get_num_words(text))            # imported from stats.py
    counts = get_char_count(text)
    sorted_list = sort_character_counts(counts)

    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()