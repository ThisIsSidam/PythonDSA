# Name : Anshu Kumar Singh
# Date : 16/12/23
# Title : Basic Sorts: Insertion Sort

'''
In insertion sort, we start from the second element in the list. We check if the
element is smaller than the previous element and switch if true. We keep doing it 
until the list is sorted.
'''

def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while temp < lst[j] and j > -1:
            lst[j+1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst
