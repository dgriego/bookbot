# print contents of frankenstein STDOUT
#
#
import re

def char_count(book_text):
    count = {}

    try:
        for i in range(0, len(book_text)):
            char = book_text[i].lower()

            if not re.match("[a-z]", char):
                continue

            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    except Exception as e:
        print(e)

    return count


def word_count(book_text):
    return len(book_text.split())


def print_report(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in document")
    print("\r")
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")
    print("\r")
    print("--- End report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(word_count(file_contents), char_count(file_contents))


main()
