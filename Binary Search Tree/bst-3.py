class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
def checkIfValidBST(root):
    return helper(root, float('-inf'), float('inf')) # Use Python's built-in representation for negative and positive infinity
 
def helper(node, min_val, max_val):
    # Base case
    if node is None:
        return True
 
    value = node.value
    # The current node's value must be between min_val and max_val
    if value <= min_val or value >= max_val: 
        return False
 
    # Check if the left and right subtrees are valid BSTs
    # The left subtree's values must all be less than the current node's value
    # The right subtree's values must all be greater than the current node's value
    isLeftBST = helper(node.left, min_val, value) # Time complexity is O(n/2)
    isRightBST = helper(node.right, value, max_val) # Time complexity is O(n/2)
 
    return isLeftBST and isRightBST # Combine two results
 
# Final time complexity is O(n), where n is the total number of nodes in the tree.
# This is because each node is visited once during the traversal.