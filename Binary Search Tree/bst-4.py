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
    isLeftBST = helper(node.left, min_val, value) # Space complexity is O(n/2) for the recursive call stack
    isRightBST = helper(node.right, value, max_val) # Space complexity is O(n/2) for the recursive call stack
 
    return isLeftBST and isRightBST # Combine two results
 
# Final space complexity is O(h), where h is the height of the tree.
# This is because the maximum amount of space is used when the recursion goes the deepest, which happens to be the height of the tree.