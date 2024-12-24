# Python - Insert: inserts elements from an array into a binary tree level by level.



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class BinaryTree:
    def __init__(self):
        self.root = None
 
    def insert(self, array):
        if len(array) == 0:
            return
        
        i = 0
 
        # If root is null
        if self.root is None:
            if array[0] is None:
                return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array):
                    return self
        
        # Insert elements
        queue = [self.root]
        while queue:
            current = queue.pop(0)
 
            # Process left child
            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array):
                    return self
            if current.left is not None:
                queue.append(current.left)
 
            # Process right child
            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array):
                    return self
            if current.right is not None:
                queue.append(current.right)
 
# Create a binary tree and insert elements
tree = BinaryTree()
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])