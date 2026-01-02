from stats import *
import sys
if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main():
    filepath = sys.argv[1]
    text = get_book_here(filepath)
    num_words = get_num_words(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")


    print("--------- Character Count -------")
    count = count_char(text)
    sorted_dict = sorting_dict(count)

    for item in sorted_dict:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()