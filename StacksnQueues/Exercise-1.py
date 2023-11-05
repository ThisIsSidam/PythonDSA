# Name : Anshu Kumar Singh
# Date : 05/11/23
# Title : Exercise 1 - Stack class with list.

'''
Create the Stack class again but using a list. Add pop and push methods.
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

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop())

print("\nStack after pop():")
my_stack.print_stack()
