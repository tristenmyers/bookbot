import sys
from stats import number_of_words
from stats import character_count
from stats import sorted_list
from stats import print_report

def get_book_text(book): #turns book text into string
    with open(book) as f:
        book_text = f.read()
    return book_text




def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = number_of_words(book_text)
    characters = character_count(book_text)    
    sorted_dictionary_list = sorted_list(characters)#test
    print_report(word_count,sorted_dictionary_list)

main()