# Name : Anshu Kumar Singh
# Date : 25/12/23
# Title : Exercise 1 - Validate BST

'''
You are tasked with writing a method called is_valid_bst in the BinarySearchTree class 
that checks whether a binary search tree is a valid binary search tree.

Your method should use the dfs_in_order method to get the node values of the binary 
search tree in ascending order, and then check whether each node value is greater than 
the previous node value.

If the node values are not sorted in ascending order, the method should return False, 
indicating that the binary search tree is not valid.

If all node values are sorted in ascending order, the method should return True, 
indicating that the binary search tree is a valid binary search tree.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while True: 
            if temp.value == new_node.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value == temp.value:
                return True

            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return False
    
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def is_valid_bst(self):
        values = self.dfs_in_order()

        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False
        return True
    


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BST is valid:")
print(my_tree.is_valid_bst())

