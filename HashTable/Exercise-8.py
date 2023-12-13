# Name : Anshu Kumar Singh
# Date : 06/12/23
# Title : Exercise 8 - Has Unique Characters

'''
Write a function called has_unique_chars that takes a string as input and 
returns True if all the characters in the string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while 
has_unique_chars('hello') should return False.
'''

def has_unique_chars(str):
    char = {}
    for letter in str:
        if letter in char:
            return False
        char[letter] = True
    return True

str1 = 'abcdefg'
str2 = 'hello'
print(has_unique_chars(str1))
print(has_unique_chars(str2))

