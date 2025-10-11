# I added the append_random_words function and made it read from the wordlist.txt file.
"""
Author: James Michelson
Purpose: Demonstrate default parameters and pass by reference.
"""

import random

def main():
    numbers_list = [10.7, 42.3, 36.1]
    word_list = ["alpha", "bravo", "charlie"]
    print(numbers_list)
    append_random_numbers(numbers_list)
    print(numbers_list)
    append_random_numbers(numbers_list, 3)
    print(numbers_list)

    print(word_list)
    append_random_words(word_list)
    print(word_list)
    append_random_words(word_list, 3)
    print(word_list)

def append_random_numbers(numbers, quantity=1):
    for i in range(quantity):
        num = round(random.uniform(0, 100), 1)
        numbers.append(num)
    
def append_random_words(words_list, quantity=1):
    for i in range(quantity):
        with open("codealong/wordlist.txt", "r") as file:
            words = file.readlines()
            new_word = words[random.randint(0, len(words))]
            words_list.append(new_word.strip())
if __name__ == "__main__":
    main()