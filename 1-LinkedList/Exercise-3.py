# Name : Anshu Kumar Singh
# Date : 20/10/23
# Title : Exercise 3 - Remove Duplicates

'''
You are given a singly linked list that contains integer values, where some of these values may be duplicated.

Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all 
duplicate values from the list.

Your method should not create a new list, but rather modify the existing list in-place, preserving the 
relative order of the nodes.
'''

# The covered area has already written class and class members. The method from the exercise is written
# below the covered area.
# -------------------------------------------------------------------------------------------------------

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

# -------------------------------------------------------------------------------------------------------

    def remove_duplicates(self):
        index = 0
        temp = self.head

        values = set()

        while temp is not None:
            if temp.value in values:
                temp = temp.next
                self.remove(index)
                continue
        
            values.add(temp.value)
            temp = temp.next
            index += 1

ll = LinkedList(0)
for i in range(1, 4):
    ll.append(i)

for i in range(2, 9):
    ll.append(i)

ll.append(6)

ll.print_list()
print("-- Removed --")

ll.remove_duplicates()
ll.print_list()

