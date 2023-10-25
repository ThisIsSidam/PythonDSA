# Name : Anshu Kumar Singh
# Date : 22/10/23
# Title : Exercise 6 - Partition List

'''
You are given a singly linked list implementation in Python that does not have a tail pointer 
(which will make this method simpler to implement).

You are tasked with implementing a method partition_list(self, x) that will take an integer x and 
partition the linked list such that all nodes with values less than x come before nodes with values
greater than or equal to x. You should preserve the original relative order of the nodes in each of 
the two partitions.

You need to implement this method as a method of the LinkedList class. The method should take an 
integer x as input. If the linked list is empty, the method should return None.

To implement this method, you should create two new linked lists. These two linked lists will be made
up of the original nodes from the linked list that is being partitioned, one for nodes less than x and
one for nodes greater than or equal to x.  None of the nodes from the linked list should be duplicated.

The creation of a limited number of new nodes is allowed (e.g., dummy nodes to facilitate the partitioning
process).

You should then traverse the original linked list and append each node to the appropriate new linked list.

Finally, you should connect the two new linked lists together.
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

    def partition_list(self, x):
        if self.head is None:
            return None

        temp = self.head
        first = LinkedList(0)
        second = LinkedList(0)
        f_temp = first.head
        s_temp = second.head

        while temp is not None:
            if temp.value < x:
                f_temp.next = temp
                f_temp = f_temp.next
                temp = temp.next
            else:
                s_temp.next = temp
                s_temp = s_temp.next
                temp = temp.next

        s_temp.next = None
        self.head = first.head.next
        f_temp.next = second.head.next



ll = LinkedList(2)
ll.append(4)
ll.append(7)
ll.append(3)
ll.append(8)
ll.append(6)
ll.append(5)
ll.append(1)
ll.append(9)

ll.print_list()
print("----")
ll.partition_list(5)
ll.print_list()

# I had a lot of problem with this one becuase I had mistakenly set s_temp to 
# first.head instead of second.head and just kept scratching my head thinking 
# why the code isn't running properly. Noticed it and all was good.
