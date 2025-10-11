"""
Author: James Michelson
Purpose: Checks the password of a user to determine it's strength and complexity
"""

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def main():
    """
    Provides the user input loop. The loop asks the user for a password to test.
    If that password is anything but "q" or "Q" call the password_strength function and report the results to the user.
    If the user enters "q" or "Q", quit the program.
    """

    while True:
        password = input("Enter a password to test: ")
        if password == "q" or password == "Q":
            break
        else:
            password_strength(password)

    pass

def word_in_file(word, filename, case_sensitive=False):
    """
    This function reads a file (specified by the filename parameter) in which each line of the file contains a single word.
    If the word passed in the word parameter matches a word in the file the function returns a true otherwise it returns a false.
    If the parameter case_sensitive is true a case sensitive match is performed. If case_sensitive is false a case insensitive match is performed.
    The case_sensitive parameter should default to False
    """

    with open(filename, "r",encoding="utf-8") as f:
        if case_sensitive == True:
            if word in f.read():
                return True
            else:
                return False
        if case_sensitive == False:
            if word.lower() in f.read():
                return True
            else:
                return False

    #return boolean

def word_has_character(word, character_list):
    """
    This function loops through each character in the string passed in the word parameter to see if that character is in the list of characters
    passed in the character_list parameter. If any of the characters in the word are present in the character list return a true,
    If none of the characters in the word are in the character list return false
    """
    value = False
    for i in word:
        if i in character_list:
            value = True
    return value

def word_complexity(word):
    """
    This function creates a numeric complexity value based on the types of characters the word parameter contains.
    One point of complexity is given for each type of character in the word.
    The function calls the word_has_character function for each of the 4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL).
    If the word has that kind of character a point is added to complexity rating.
    Since there are 4 kinds of characters the complexity rating will range from 0 to 4.
    (0 would be returned only if word contained no characters or only contains characters that are not in any of the lists.)
    """
    word_complexity = 0
    if word_has_character(word, LOWER) == True:
        word_complexity += 1

    if word_has_character(word, UPPER) == True:
        word_complexity += 1

    if word_has_character(word, DIGITS) == True:
        word_complexity += 1

    if word_has_character(word, SPECIAL) == True:
        word_complexity += 1

    return int(word_complexity)


def password_strength(password, min_length=10, strong_length=16):
    """
    This function checks length requirements, checks dictionary and known-passwords,
    calls word_complexity to calculate the word's complexity then determines the password's strength based on the user requirements.
    It should print the messages defined in the requirements and return the password's strength as a number from 0 to 5.
    The min_length parameter should have a default value of 10. The strong_length parameter should have a default value of 16
    """

    if word_in_file(password, "week02/wordlist.txt", False) == True:
        complexity = 0
        print("Password is a dictionary word and is not secure.")
        print(f"Password complexity: {complexity}")
        return complexity
    
    if word_in_file(password, "week02/toppasswords.txt", True) == True:
        complexity = 0
        print("Password is a commonly used password and is not secure.")
        print(f"Password complexity: {complexity}")
        return complexity

    if len(password) < 10:
        complexity = 1
        print("Password is too short and is not secure.")
        print(f"Password complexity: {complexity}")
        return complexity

    if len(password) > 15:
        complexity = 5
        print("Password is long, length trumps complexity this is a good password")
        print(f"Password complexity: {complexity}")
        return complexity

    else:
        complexity = word_complexity(password)
        print("This is an acceptable password")
        print(f"Password complexity is {complexity}")
        return complexity

if __name__ == "__main__":
    main()