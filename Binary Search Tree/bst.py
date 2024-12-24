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
 
    # The middle element of the array becomes the root of the tree
    middle = (left + right) // 2  # Time complexity of this operation is O(1)
    node = Node(nums[middle])  # Time complexity of this operation is O(1)
 
    # Recursively build the left and right subtrees
    # As this operation is performed recursively on each half of the array,
    # its time complexity is O(n), where n is the number of elements in the array
    node.left = buildBSTfromSortedArray(nums, left, middle - 1)
    node.right = buildBSTfromSortedArray(nums, middle + 1, right)
 
    # At this point, the tree has been constructed
    return node
 
# Final time complexity: O(n)