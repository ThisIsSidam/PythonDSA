# Name : Anshu Kumar Singh
# Date : 04/12/23
# Title : Exercise 5 - Two Sum

'''
Problem: Given an array of integers nums and a target integer , find the indices of two 
numbers in the array that add up to the target.

Input:
A list of integers nums .
A target integer target.

Output:
A list of two integers representing the indices of the two numbers in the input array nums 
that add up to the target. If no two numbers in the input array add up to the target, 
return an empty list [].

Example:

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: The numbers at indices 0 and 1 in the array add up to the target 9.
 
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: The numbers at indices 1 and 2 in the array add up to the target 6.
'''

def two_sum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement], i]
        nums_map[num] = i
    return []

ls = [2, 7, 11, 15]
tar = 9

print(two_sum(ls, tar))