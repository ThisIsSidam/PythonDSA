# Name : Anshu Kumar Singh
# Date : 01/01/24
# Title : Exercise 3 - Validate BST

'''
Given a sorted list of integers, rearrange the list in-place such that all unique elements 
appear at the beginning of the list, followed by the duplicate elements. Your function 
should return the new length of the list containing only unique elements. Note that you 
should not create a new list or use any additional data structures to solve this problem. 
The original list should be modified in-place.

Constraints:

The input list is sorted in non-decreasing order.
The input list may contain duplicates.
The function should have a time complexity of O(n), where n is the length of the input list.
The function should have a space complexity of O(1), i.e., it should not use any additional 
data structures or create new lists.


Example:
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] 
Function call: new_length = remove_duplicates(nums) 
Output: new_length = 5 
Modified list: nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] (first 5 elements are unique)

Explanation: The function modifies the original list nums in-place, moving unique elements 
to the beginning of the list, followed by duplicate elements. The new length returned by 
the function is 5, indicating that there are 5 unique elements in the list. The first 5 
elements of the modified list nums are the unique elements [0, 1, 2, 3, 4].
'''

def remove_duplicates(numbers):
    if len(numbers) == 0:
        return 0
    
    new_length = 1
    move_here_index = 1
    for num in numbers:
        if num > numbers[move_here_index-1]:
            numbers[move_here_index] = num
            new_length += 1
            move_here_index += 1
    return new_length


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])
