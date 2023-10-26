# Name : Anshu Kumar Singh
# Date : 26/10/23
# Title : Exercise 2 - Reverse

'''
Create a new method called reverse that reverses the order of the nodes in the list, 
i.e., the first node becomes the last node, the second node becomes the second-to-last
node, and so on.

To do this, you'll need to traverse the list and change the direction of the pointers 
between the nodes so that they point in the opposite direction. Once you've done this 
for all nodes, you'll also need to update the head and tail pointers to reflect the 
new order of the nodes.
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

    def reverse(self):
        temp = self.head

        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        
        self.head, self.tail = self.tail, self.head


dll = DoublyLinkedList(0)
for i in range(1, 5):
    dll.append(i)

dll.print_list()
print("-")

dll.reverse()
dll.print_list()

'''
Seems the super easy previous exercise was a trailer for this movie because I was 
able to successfully create the function but a bit longer. I underestimated the
swapping power of python. 
'''