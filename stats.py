def number_of_words(book_text):#calculates num of words
    word_count = 0
    split_words = book_text.split()
    for word in split_words:
        word_count += 1
    return word_count

def check_for_entries(sys):#checks that the command has proper arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def character_count(book_text):
    character_dictionary = {}
    lowercase_text = book_text.lower()
    for character in lowercase_text:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary

def sort(dictionary_list):#tells value to sort by making a list of nums
    character_list = []
    for pair in dictionary_list:
        value = dictionary_list[pair]
        character_list.append(value)
    return character_list

def sorted_list(character_dictionary):
    list_of_dictionaries = []
    for dict in character_dictionary:
        value = character_dictionary[dict]
        new_dict = {dict:value}#creates individual dictionaries for list
        list_of_dictionaries.append(new_dict)
    list_of_dictionaries.sort(reverse=True, key=sort)#BROKEN
    return list_of_dictionaries

def print_report(wordcount,sorted_dictionary_list,book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for value in sorted_dictionary_list:
        for key in value:
            if key.isalpha() == True:
                letter = key
                num = value[key]
                print(f"{letter}: {num}")
    print("============= END ===============")
