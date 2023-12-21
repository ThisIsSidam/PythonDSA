# Name : Anshu Kumar Singh
# Date : 21/12/23
# Title : Quick Sort

'''
In quick sort,  we start from the first index, we call that pivot point, pointed by pivot_index
variable. There is also swap_index variable on pivot point. And an i variable next to it. We start
checking if the value at i is greater than or smaller than the value at pivot point. We don't do
anything if the value is greater than pivot point, just move i. If the value is smaller, we move 
the swap_index ahead one step and do a swap values between i and swap_index.

This way the whole list gets separated into three zones. First is the pivot point in the start. 
Second is the values less than pivot point and then the values larger than pivot point. swap_index would 
always stay at the last index of the smaller value's zone, and moves ahead to start of larger value
zone every time a new small value is found, and then switches. 

In the end, pivot_index will be at the start, swap_index will be at the end of small value zone. While i 
will be at the end of the list. Then we'll swap values between pivot_index and swap_index. Moving the 
pivot in the middle would make it sorted in the list. 

Then we use the quick_sort method again on both parts of the list. Keeping at it until the lists have
only one element.
'''

def pivot(lst, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if lst[i] < lst[pivot_index]:
            swap_index += 1
            lst[i], lst[swap_index] = lst[swap_index], lst[i]

    lst[pivot_index], lst[swap_index] = lst[swap_index], lst[pivot_index]
    return swap_index

def quick_sort_helper(lst, left, right):
    if left < right:
        pivot_index = pivot(lst, left, right)
        quick_sort_helper(lst, left, pivot_index-1)
        quick_sort_helper(lst, pivot_index+1, right)

    return lst

def quick_sort(lst):
    return quick_sort_helper(lst, 0, len(lst) -1)


'''
BigO of Quick Sort

We go through the whole list, which makes it O(n).
Then we start going through pieces of it, which makes it O(logn)

In the end, it is O(n*logn)

In worst case scenario when the data is already sorted, it is O(n^2).
Because with unsorted data, pivot point is set to middle breaking the list in two
parts that quickly keep getting smaller. But in case of already sorted data, the left part
which is already sorted, won't get sent to middle, the list won't break into two.
We'll run it again on again with the right part of the list which is the entire list 
with only one element getting removed each time.
'''