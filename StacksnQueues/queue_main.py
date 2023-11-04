# Name : Anshu Kumar Singh
# Date : 03/11/23
# Title : Queue

'''
Think of queues like cars in a drivethrough.

The first in the queue gets served first and gets out of the queue first.
But the ones coming are in the last.

We call this FIFO, First In First Out.

We'll create this from a Linked List. Head becomes first, and tail becomes last.

Different Data Structures have different terminology. The push or add method in 
queue is called enqueue, while the pop or remove method is called dequeue. 

The enqueue method will be like, pushing or adding into the queue while the term
used for popping or removing is dequeue.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_list(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else: 
            self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp
    