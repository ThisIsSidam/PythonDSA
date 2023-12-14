# Name : Anshu Kumar Singh
# Date : 10/11/23
# Title : Exercise 3 - First Non-repeating character

'''
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first 
non-repeating character in the given string using a hash table (dictionary). 
If there is no non-repeating character in the string, the function should return 
None.

For example, if the input string is "leetcode", the function should return "l" 
because "l" is the first character that appears only once in the string. 
Similarly, if the input string is "hello", the function should return "h" because
"h" is the first non-repeating character in the string.
'''

def first_non_repeating_char(str):
    str_char = {}
    for char in str:
        str_char[char] = str_char.get(char, 0) + 1

    for char in str:
        if str_char[char] == 1:
            return char
        
    return None
        
hey = "helloh"
print(first_non_repeating_char(hey))
empty = ""
print(first_non_repeating_char(empty))