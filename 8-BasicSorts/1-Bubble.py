# Name : Anshu Kumar Singh
# Date : 16/12/23
# Title : Basic Sorts: Bubble Sort

'''
In bubble sort, we start from the first element, check if it's bigger
than the second one or not and move it accordingly. The biggest one is
pushed to the end. Then we start again, but stop at the second last 
because we already know that the last one is the largest. We repeat
the process until the list is completely sorted.
'''

def BubbleSort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

    return lst

