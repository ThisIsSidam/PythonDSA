# Name : Anshu Kumar Singh
# Date : 06/11/23
# Title : Exercise 5 - Queue with two stacks

'''
You are given a class MyQueue which implements a queue using two stacks. Your task 
is to implement the enqueue method which should add an element to the back of the queue.

To achieve this, you can use the two stacks stack1 and stack2. Initially, all elements 
are stored in stack1 and stack2 is empty. In order to add an element to the back of the
queue, you need to first transfer all elements from stack1 to stack2 using a loop that 
pops each element from stack1 and pushes it onto stack2.

Once all elements have been transferred to stack2, push the new element onto stack1. 
Finally, transfer all elements from stack2 back to stack1 in the same way as before,
 so that the queue maintains its ordering.

Your implementation should satisfy the following constraints:

The method signature should be def enqueue(self, value).

The method should add the element value to the back of the queue.

The method should run in constant time complexity, O(1).
'''

class Stack: 
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) -1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        self.stack_list.append(value)

    def is_empty(self):
        return len(self.stack_list) == 0
            
    def size(self):
        return len(self.stack_list)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def pop(self):
        if self.is_empty():
            return None
        temp = self.stack_list[self.size() -1]
        self.stack_list.pop(self.size() -1)
        return temp


class MyQueue:
    def __init__(self, value):
        self.stack1 = Stack()
        self.stack2 = Stack()

        self.stack1.push(value)
        self.length = 1

    def print_queue(self):
        self.stack1.print_stack()

    def enqueue(self, value):
        if self.stack1.is_empty():
            self.stack1.push(value)
            return False

        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        self.stack1.push(value)

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())      

        self.length += 1
        return True
    
    def dequeue(self):
        return self.stack1.pop()


q = MyQueue(5)
q.enqueue(4)
q.enqueue(7)
q.print_queue()
print("--")
print(f"Popped {q.dequeue()}")
print("--")
q.print_queue()
