# Name : Anshu Kumar Singh
# Date : 16/12/23
# Title : Basic Sorts: Selection Sort

'''
In selection sort, we take the first element, and then go through the list saving the smallest
element's index in the min_index variable. If there indeed was a element smaller than the 
first one, we switch the values and move to second element and redo the process.
'''

def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
            
        if i is not min_index:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp
    return lst


