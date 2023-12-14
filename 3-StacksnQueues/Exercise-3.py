# Name : Anshu Kumar Singh
# Date : 05/11/23
# Title : Exercise 3 - Reverse String

'''
The reverse_string function takes a single parameter string, which is the string you 
want to reverse.

Return a new string with the letters in reverse order.

Use the List Based Stack class for this.
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

def reverse_string(string):
    stack = Stack()
    for str in string:
        stack.push(str)
    
    reverse = ""
    while not stack.is_empty():
        reverse += stack.pop()
    
    return reverse

print("Enter a string: ", end="")
string = input()

print(reverse_string(string))

# Easily Done. Feeling happy since I couldn't do the previous one.
