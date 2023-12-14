# Name : Anshu Kumar Singh
# Date : 22/10/23
# Title : Exercise 5 - Reverse Between

'''
You are given a singly linked list and two integers m and n. Your task is to write a method 
reverse_between within the LinkedList class that reverses the nodes of the linked list from 
index m to index n (inclusive) in one pass and in-place.

Input----
The method reverse_between takes two integer inputs m and n.
The method will only be passed valid indexes (you do not need to test whether the indexes are
out of bounds)

Output----
The method should modify the linked list in-place by reversing the nodes from index m to index n.
If the linked list is empty or has only one node, the method should return None.

Example----
Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4. Then, the method should 
modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .

Constraints----
The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space 
complexity of O(1).
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

    def reverse_between(self, m, n):
        if self.length == 0 or self.length == 1:
            return False
        
        index = m
        pre_cutoff = self.get(m-1)
        before = temp = after = pre_cutoff.next

        # Using the same action we did in reverse method.
        while index != n+1:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            index += 1

        pre_cutoff.next.next = temp
        pre_cutoff.next = before
        return True

ll = LinkedList(0)
for i in range(1, 5):
    ll.append(i)


ll.print_list()
print("----")
print(ll.reverse_between(2, 3))
ll.print_list()

'''
This is the first exercise I used a notebook with and succeeded in the first try.
I'm very happy about this.

I used the same action used in the reverse method. On the notebook, I cut off the 
other parts of the LinkedList (Not actually) from the part I had to reverse. That 
is why one of the nodes is called pre_cutoff, it's the one right before the m index.

I reverse and then join the ends. Done.

Also it made more sense with returning Boolean values instead of None. So I did.
'''


        





