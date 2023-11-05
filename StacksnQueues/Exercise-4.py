# Name : Anshu Kumar Singh
# Date : 05/11/23
# Title : Exercise 4 - Sort Stack


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

def sort_stack(stack):
    stack2 = Stack()

    # stack2.push(stack.pop())
    while not stack.is_empty():
        temp = stack.pop()
        while not stack2.is_empty() and stack2.peek() > temp:
            stack.push(stack2.pop())
        stack2.push(temp)
    
    while not stack2.is_empty():
        stack.push(stack2.pop())

st = Stack()
st.push(3)
st.push(5)
st.push(4)
st.push(7)

st.print_stack()
print("-----")
sort_stack(st)
st.print_stack()
    
        