# Name : Anshu Kumar Singh
# Date : 17/12/23
# Title : Exercise 3 - Insertion Sort on LL

'''
Write an insertion_sort() method in the LinkedList class that will sort the elements of a linked list 
in ascending order using the insertion sort algorithm.

The method should update the head and tail pointers of the linked list to reflect the new order of 
the nodes in the list.

You can assume that the input linked list will contain only integers. You should not use any 
additional data structures to sort the linked list.

Input:
The LinkedList object containing a linked list with unsorted elements (self).

Output:
None. The method sorts the linked list in place.

Method Description:

If the length of the linked list is less than 2, the method returns and the list is assumed to be 
already sorted.

The first element of the linked list is treated as the sorted part of the list, and the second 
element is treated as the unsorted part of the list.

The first element of the sorted part of the list is then disconnected from the rest of the list, 
creating a new linked list with only one element.

The method then iterates through each remaining node in the unsorted part of the list.

For each node in the unsorted part of the list, the method determines its correct position in the 
sorted part of the list by comparing its value with the values of the other nodes in the sorted part 
of the list.

Once the correct position has been found, the node is inserted into the sorted part of the list at 
the appropriate position.

After all the nodes in the unsorted part of the list have been inserted into the sorted part of the 
list, the head and tail pointers of the linked list are updated to reflect the new order of the nodes 
in the list.

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

    def insertion_sort(self):
        if self.length < 2:
            return

        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None

        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next

            prev = sorted_list_head
            while prev is not None:
                next = prev.next
                if prev.value > current.value:
                    sorted_list_head = current
                    current.next = prev
                    break
                if next is None:
                    prev.next = current
                    current.next = None
                    self.tail = current
                    break
                if current.value > prev.value and current.value < next.value:
                    prev.next = current
                    current.next = next
                    break
                prev = prev.next

        self.head = sorted_list_head

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()
