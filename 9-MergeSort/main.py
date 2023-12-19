# Name : Anshu Kumar Singh
# Date : 19/12/23
# Title : Merge Sort

'''
In merge sort we break the list until there are multiple lists of single elements. 
Then we pick out two elements and join then in order. Make 2 element sorted lists.
Then keep joining like this until the whole list is complete and sorted.

Merging is done separately in a helper function called, Merge. 
'''

def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(list):
    if len(list) == 1:
        return list
    middle_index = int(len(list)/2)
    left_list = merge_sort(list[:middle_index])
    right_list = merge_sort(list[middle_index:])

    return merge(left_list, right_list)



