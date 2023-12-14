# Name : Anshu Kumar Singh
# Date : 26/10/23
# Title : Exercise 4 - Swap Pairs

'''
Implement a method called swap_pairs within the class that swaps the values of adjacent 
nodes in the linked list. The method should not take any input parameters.

Note: This DoublyLinkedList does not have a tail pointer which will make the 
implementation easier.

Example:

1-->2-->3-->4--> should become 2-->1-->4-->3-->

Your implementation should handle edge cases such as an empty linked list or a linked 
list with only one node.

Note: You must solve the problem without modifying the values in the list's nodes 
(i.e., only the nodes' prev and next pointers may be changed.)
'''

# The covered area has already written class and class members. The method from the
# exercise is written below the covered area.
# ----------------------------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next  

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node 
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else: 
            temp = self.tail
            for _ in range (self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return False
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()

        temp = self.get(index)
        before = temp.prev
        after = temp.next

        before.next = after
        after.prev = before

        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp.value
    
# ----------------------------------------------------------------------------------

    def swap_pairs(self):
        if self.length == 0 or self.length == 1:
            return 
        temp1 = self.head
        temp2 = temp1.next
        dummy1 = None
        dummy2 = temp2.next

        self.head = temp2

        while temp1 and temp2:
            dummy1 = temp1.prev
            dummy2 = temp2.next

            temp2.prev = temp1.prev
            temp1.next = temp2.next
            temp1.prev = temp2
            temp2.next = temp1

            if dummy1:
                dummy1.next = temp2
            if dummy2:
                dummy2.prev = temp1
            
            temp1 = temp1.next
            if temp1:
                temp2 = temp1.next
            else: 
                temp2 = None
            

dll = DoublyLinkedList(0)
for i in range(1, 9):
    dll.append(i)

print('--')
dll.print_list()

# Test Case 1: Odd Length
dll.swap_pairs()
print('--')
dll.print_list()

# Test Case 2: Even Length
dll.append(9)
dll.swap_pairs() # Old part was already swapped so will get back to normal.
print('--')
dll.print_list()



