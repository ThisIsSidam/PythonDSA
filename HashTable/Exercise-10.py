# Name : Anshu Kumar Singh
# Date : 06/12/23
# Title : Exercise 10 - Longest Consecutive Sequence

'''
Given an unsorted array of integers, write a function that finds the length of the  
longest_consecutive_sequence (i.e., sequence of integers in which each element is 
one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.
Output: An integer representing the length of the longest consecutive sequence in 
nums.

Example:

Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], 
and its length is 4.
'''

def longest_consecutive_sequence(nums):
    set1 = sorted(set(nums))
    count = 0
    for i, num in enumerate(set1):
        if (num == set1[i+1] + 1):
            count += 1
        else:
            count = 0
    return count

nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(nums))
