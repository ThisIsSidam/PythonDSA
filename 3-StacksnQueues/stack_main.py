# Name : Anshu Kumar Singh
# Date : 03/11/23
# Title : Stack

'''
Picture it like a stack of books. One is on top of another. 

When you have two books in a stack, you can't get the first one without first taking out
the second one (Which is on top of the first one).

This is called LIFO : Last In First Out. The last one going in the stack will be the first
one to come out.

This Data Structure would be implemented using Linked List. 

The head of the list would become the top of the stack while the tail would become the 
bottom of the stack. Although we won't be using the bottom as it doesn't have any uses.

It is not the other way around because unlike the tail of the list, Adding and Removing 
from the head of the list is O(1), which is more like the pushing and popping from the top
of a stack.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def __init__(self):
        self.top = None
        self.height = 0

    def is_empty(self):
        return self.height == 0

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        
        self.height -= 1
        return temp

    
        
