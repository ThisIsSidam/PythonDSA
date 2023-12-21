# Name : Anshu Kumar Singh
# Date : 19/12/23
# Title : Merge function for LL

'''
The merge method takes in another LinkedList as an input and merges it with the current 
LinkedList. The elements in both lists are assumed to be in ascending order, but the input 
lists themselves do not need to be sorted.

Parameters:
other_list (LinkedList): the other LinkedList to merge with the current list

Return Value:
This method does not return a value, but it modifies the current LinkedList to contain the 
merged list.

Example:

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)
 
l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)
 
l1.merge(l2)
 
# The current list (l1) now contains the merged list [1, 2, 3, 4, 5, 6, 7, 8]
'''

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

    def merge(self, other_list):
        dummy = Node(None)
        current = dummy

        i = self.head
        j = other_list.head

        while i is not None and j is not None:
            if i.value < j.value:
                current.next = i
                current = i
                i = i.next
            else:
                current.next = j
                current = j
                j = j.next
        if i is not None:
            current.next = i
        if j is not None:
            current.next = j
        self.head = dummy.next
        if other_list.tail.value < self.tail.value:
            self.tail = other_list.tail
        self.length += other_list.length        


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()
