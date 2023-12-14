# Name : Anshu Kumar Singh
# Date : 20/10/23
# Title : Exercise 4 - Find Kth Element From the End

'''
Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.

Your task is to write a program that takes as input a linked list and a number k, and returns the item that 
is k steps away from the end of the list. If the linked list has fewer than k items, the program should 
return None.
'''

from main import LinkedList # Not a class method, so we can remove the class code and just import.

# Sadly, I wasn't able to solve this one.

def find_kth_from_end(linkedlist, k):
    slow = fast = linkedlist.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next

    return slow

ll = LinkedList(0)
for i in range(1, 10):
    ll.append(i)

ll.print_list()
print("----")

print("Last element: ", find_kth_from_end(ll, 1).value)
print("First element: ", find_kth_from_end(ll, 10).value)
print("6th from end: ", find_kth_from_end(ll, 6).value)
