# Part 1: Code with Comments explaining Time Complexity

# Part 2: Code with Comments explaining Space Complexity

# Part 1 -

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
 
# Creating the list
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node('a')
head.next.next.next.next.next = Node('a')
 
 
def removeDupes(head):
    # Time Complexity Explanation: 
    # The function contains a while loop that traverses the linked list once, so the time complexity is O(n) 
    # where n is the number of nodes in the linked list.
    
    curr = head
    while curr:
        nextDistinctVal = curr.next
        while nextDistinctVal is not None and curr.val == nextDistinctVal.val:
            nextDistinctVal = nextDistinctVal.next
        curr.next = nextDistinctVal
        curr = nextDistinctVal
    return head
# Time complexity of this function is O(n), where n is the number of nodes in the list
 
removeDupes(head)
# Part 2-

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
 
# Creating the list
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node('a')
head.next.next.next.next.next = Node('a')
 
 
def removeDupes(head):
    # Space Complexity Explanation: 
    # This function uses a constant amount of space to store the 'head', 'curr' and 'nextDistinctVal' pointers. 
    # Therefore, the space complexity is O(1).
    
    curr = head
    while curr:
        nextDistinctVal = curr.next
        while nextDistinctVal is not None and curr.val == nextDistinctVal.val:
            nextDistinctVal = nextDistinctVal.next
        curr.next = nextDistinctVal
        curr = nextDistinctVal
    return head
# Space complexity of this function is O(1), as it uses a constant amount of space
removeDupes(head)