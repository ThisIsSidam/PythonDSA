# Name : Anshu Kumar Singh
# Date : 26/10/23
# Title : Exercise 3 - Is Palindrome

'''
Write a method to determine whether a given doubly linked list reads the same forwards 
and backwards.

For example, if the list contains the values [1, 2, 3, 2, 1], then the method should 
return True, since the list is a palindrome.

If the list contains the values [1, 2, 3, 4, 5], then the method should return False, 
since the list is not a palindrome.
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

    def is_palindrome(self):
        f_temp = self.head
        b_temp = self.tail

        front_list = []
        back_list = []
        for _ in range(int(self.length/2)):
            front_list.append(f_temp.value)
            back_list.append(b_temp.value)

        return front_list == back_list

# True Case 1: Odd Length
dll_1 = DoublyLinkedList(1)
dll_1.append(2)
dll_1.append(3)
dll_1.append(2)
dll_1.append(1)
print("--")
dll_1.print_list()
print(dll_1.is_palindrome())

# True Case 2: Even Length
dll_2 = dll_1
dll_2.insert(3, 3)
print("--")
dll_2.print_list()
print(dll_2.is_palindrome())

# False Case
dll_3 = DoublyLinkedList(0)
for i in range(1, 10):
    dll_3.append(i)

print("--")
dll_3.print_list()
print(dll_3.is_palindrome())

'''
I was quite proud of my method until I checked the solution. 

The solution's method matches the values right in the loop and return false the moment
they don't match, and don't put them in a list.

The whole idea of adding the values into the list came when I was thinking about going 
through the list twice. But thought of going through the list once with two pointers 
on each side, but didn't remove the list from the plan. 
'''