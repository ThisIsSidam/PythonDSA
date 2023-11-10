# Name : Anshu Kumar Singh
# Date : 10/11/23
# Title : Exercise 2 - Find Duplicates

'''
Problem: Given an array of integer nums, find all the duplicates in the array 
using a hash table (dictionary).

Input: A list of integer nums.

Output: A list of integers representing the numbers in the input array nums that 
appear more than once. If no duplicates are found in the input array, return an 
empty list [].

Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
Explanation: The numbers 2 and 3 appear more than once in the input array.
'''

def find_duplicates(list):
    dict = {}
    for num in list:
        dict[num] = dict.get(num, 0) + 1
    
    duplicates = []
    for key in dict.keys():
        if dict[key] > 1:
            duplicates.append(key)

    return duplicates
        
ls = [3, 5, 3, 4, 7, 1, 6, 3, 5]
print(find_duplicates(ls))