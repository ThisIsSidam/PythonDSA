# Name : Anshu Kumar Singh
# Date : 25/12/23
# Title : Tree Traversal

'''
Traversing a tree means going through each element of the three.
After going through the tree, the traversing method returns a list
of values in the tree.

There are two ways we can traverse a Binary Search Tree. Which are-

1. Breadth First Search- In BFS, the values are added in the returning list row by row.
First the root which is in the first row and then the left and right of root as they're 
in the second row. Then the method checks the left and right of root's left, then goes to
root's right. The returning row has elements in the same order as they were added.

2. Depth First Search- 

There are three types of Depth First Search.

1. Pre-order- Here we start by adding values to the results list while going to the left 
bottom, if there is't  a left anymore, the method moves one step back and checks for right,
adds the value of the right and then again looks at left, if there isn't any left, step back
and then right, if there isn't any left or right, step back more. Simply, first add the value
of where the current_node pointer will be, then look at left, and then look at right. 

2. Post-order- Same as pre_order, just that the values are added after the current_node 
pointer meets a deadend. Meaning, the pointer will first go to the left bottom and then
when there isn't a left anymore, the value will be added. Then step back, look at right, 
when the right also becomes a deadend, step back from right and add the value of the node
whose left and right were checked, and keep going.

3. In-order- At last, in in_order, we do things similarly to the last two. Just when there
isn't a left, we step back and before checking the right, we add the current_node's value 
and then move to right. This way the result we get is sorted.

We are going to see all of these here.
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
    
    # Breadth First Search
    def BFS(self):
        current = self.root
        queue = [] # It will be better to use the Queue Data Structure
        results = []

        queue.append(current)

        while len(queue) > 0:
            current = queue.pop(0)
            results.append(current.value)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            
        return results

    def dfs_pre_rder(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results
    
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

