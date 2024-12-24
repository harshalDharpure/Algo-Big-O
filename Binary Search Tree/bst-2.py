class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
def buildBSTfromSortedArray(nums, left=0, right=None):
    if right is None:
        right = len(nums) - 1
 
    # Base case
    if left > right: 
        return None
 
    middle = (left + right) // 2
    node = Node(nums[middle])  # Space complexity of this operation is O(1)
 
    # Recursively build the left and right subtrees
    # As this operation is performed recursively on each half of the array,
    # its space complexity is O(log(n)), where n is the number of elements in the array
    # This is due to the space required by the call stack for the recursive calls
    node.left = buildBSTfromSortedArray(nums, left, middle - 1)
    node.right = buildBSTfromSortedArray(nums, middle + 1, right)
 
    # At this point, the tree has been constructed
    return node
 
# Final space complexity: O(log(n)+ n) = O(n) ( as the BST has n elements)  