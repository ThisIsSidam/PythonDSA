# Name : Anshu Kumar Singh
# Date : 10/11/23
# Title : Exercise 1 - Common Items

'''
Write a function item_in_common(list1, list2) that takes two lists as input and returns
True if there is at least one common item between the two lists, False otherwise.

Use a dictionary to solve the problem that creates an O(n) time complexity.
'''

def item_in_common(list1, list2):
    dict = {}
    for i in list1:
        dict[i] = True
    
    for i in list2:
        if i in dict:
            return True
    return False

ls = [3, 5, 6]
ls2 = [8, 9, 4]

print(item_in_common(ls, ls2))