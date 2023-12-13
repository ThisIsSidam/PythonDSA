# Name : Anshu Kumar Singh
# Date : 05/12/23
# Title : Exercise 7 - Remove Duplicates

'''
You have been given a list my_list with some duplicate values. Your task 
is to write a Python program that removes all the duplicates from the list 
using a set and then prints the updated list.

You need to implement a function remove_duplicates(my_list) that takes in 
the input list my_list as a parameter and returns a new list with no 
duplicates.

Your function should not modify the original list, instead, it should 
create a new list with unique values and return it.

Example:

Input:
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
 
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Note:
The order of the elements in the updated list may be different from the 
original list, as sets are unordered.
'''

def remove_duplicates(my_list):
    new_set = set()
    for value in my_list:
        new_set.add(value)

    new_list = []
    for value in new_set:
        new_list.append(value)
    
    return new_list

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
print(remove_duplicates(my_list))

'''
I couldn't solve the previous exercises so got happy when I saw how easy this
one was. But checked the solution and this can be done in two lines.

def remove_duplicates(my_list):
    return list(set(my_list))
'''