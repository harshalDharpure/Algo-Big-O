# Part 1: Code with Comments explaining Time Complexity

# Part 2: Code with Comments explaining Space Complexity

# Part 3: Full code along with code to create the binary tree ( for you to try out )

# Part 1 -

def diameterBinaryTree(root):
    # If there's no root, the diameter is 0
    if not root:
        return 0
    
    maxDiameter = 0
 
    # DFS function that returns the height of the tree and updates the maximum diameter
    def dfs(node):
        nonlocal maxDiameter  # allows us to modify the outer scope's maxDiameter variable
 
        # base case: if node is null, return -1 (height of an empty tree)
        if not node: 
            return -1
 
        # Time complexity for both dfs calls combined is O(n), 
        # where n is the total number of nodes in the tree,
        # because every node in the tree is visited exactly once
        leftHeight = dfs(node.left)  # calculate height of left subtree
        rightHeight = dfs(node.right)  # calculate height of right subtree
 
        # calculate diameter and update maxDiameter if current diameter is greater
        diameter = leftHeight + rightHeight + 2  # +2 because we need to count edges, not nodes
        maxDiameter = max(maxDiameter, diameter)
 
        # return height of current node
        return max(leftHeight, rightHeight) + 1  # +1 to include the current node itself
 
    # start the dfs from root
    dfs(root)
 
    # Final time complexity is O(n) as we visit each node exactly once
    return maxDiameter


#Part 2-

def diameterBinaryTree(root):
    if not root:
        return 0
    
    maxDiameter = 0
 
    def dfs(node):
        nonlocal maxDiameter
 
        if not node: 
            return -1
 
        leftHeight = dfs(node.left)
        rightHeight = dfs(node.right)
 
        # The space complexity here is O(h) where h is the height of the tree, 
        # this is due to the extra space required by the call stack during the depth-first search.
        diameter = leftHeight + rightHeight + 2
        maxDiameter = max(maxDiameter, diameter)
 
        return max(leftHeight, rightHeight) + 1
 
    # start the dfs from root
    dfs(root)
 
    # Final space complexity is O(h) due to the maximum amount of space utilized by the call stack
    return maxDiameter
# Part 3-

# Note: In Python, a deque stands for a "double-ended queue". It's part of the collections module and provides an efficient way to handle operations at both ends of a collection. This includes operations like appending and popping elements.

# Alternatively you can implement the queue with a LL as well. In an interview you can also go ahead and implement it with an array after mentioning to the interviewer that you are doing this just to save time

from collections import deque
 
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
        if self.root is None:
            if array[0] is None:
                return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array):
                    return self
 
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array):
                    return self
            if current.left is not None:
                queue.append(current.left)
            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array):
                    return self
            if current.right is not None:
                queue.append(current.right)
 
def diameterBinaryTree(root):
    if not root:
        return 0
    maxDiameter = 0
    def dfs(node):
        nonlocal maxDiameter
        if not node:
            return -1
        leftHeight = dfs(node.left)
        rightHeight = dfs(node.right)
        diameter = leftHeight + rightHeight + 2
        maxDiameter = max(maxDiameter, diameter)
        return max(leftHeight, rightHeight) + 1
    dfs(root)
    return maxDiameter
 
tree = BinaryTree()
tree.insert([1, 3, 2, 7, 4, None, None, 8, None, None, 5, 9, None, None, 6])
print(diameterBinaryTree(tree.root))