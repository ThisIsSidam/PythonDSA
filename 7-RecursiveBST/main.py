# Name : Anshu Kumar Singh
# Date : 15/11/23
# Title : Recursive Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_bst(self):
        print("Root: ", self.root.value)
        print("root.right ", self.root.right.value)
        print("root.left ", self.root.left.value)

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return 
        self.__r_insert(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        elif value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def r_delete_node(self, value):
        self.__r_delete_node(self.root, value)

    def __r_delete_node(self, current_node, value):
        if current_node == None:
            return None
        elif value < current_node.value:
            current_node.left = self.__r_delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete_node(current_node.right, sub_tree_min)
        return current_node
    
