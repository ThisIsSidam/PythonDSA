# Name : Anshu Kumar Singh
# Date : 17/12/23
# Title : Exercise 1 - Bubble Sort on LL

'''
Write a bubble_sort() method in the LinkedList class that will sort the elements of a linked 
list in ascending order using the bubble sort algorithm. The method should update the head 
and tail pointers of the linked list to reflect the new order of the nodes in the list. You 
can assume that the input linked list will contain only integers. You should not use any 
additional data structures to sort the linked list.

Input:
The LinkedList object containing a linked list with unsorted elements (self).

Output:
None. The method sorts the linked list in place.

Method Description:

If the length of the linked list is less than 2, the method returns and the list is assumed 
to be already sorted.

The bubble sort algorithm works by repeatedly iterating through the unsorted part of the 
list, comparing adjacent elements and swapping them if they are in the wrong order.

The method starts with the entire linked list being the unsorted part of the list.

For each pass through the unsorted part of the list, the method iterates through each pair 
of adjacent elements and swaps them if they are in the wrong order.

After each pass, the largest element in the unsorted part of the list will "bubble up" to 
the end of the list.

The method continues iterating through the unsorted part of the list until no swaps are made 
during a pass.

After the linked list is fully sorted, the head and tail pointers of the linked list are 
updated to reflect the new order of the nodes in the list.

Constraints:
The linked list can contain duplicates.
The method should be implemented in the LinkedList class.
The method should not use any additional data structures to sort the linked list.
'''

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__ (self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list (self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def append (self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def prepend (self, value):
        new_node = Node(value)
         
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            pre = self.head
            while pre.next.next is not None:
                pre = pre.next
            temp = pre.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp
            
    def get(self, index):
        if index >= self.length or index < 0:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        
        pre = self.get(index -1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def bubble_sort(self):
        if self.length < 2:
            return 
        
        for i in range(self.length -1, 0, -1):
            current = self.head
            next_node = current.next
            while next_node is not None:
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                current = current.next
                next_node = current.next

            

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()


