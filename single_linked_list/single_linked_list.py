class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
 
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1
        return current
 
    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def addAtHead(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
 
    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
 
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def addAtIndex(self, index, value):
        if index < 0 or index > self.size:
            return 'invalid index'
        if index == self.size:
            return self.addAtTail(value)
        if index == 0:
            return self.addAtHead(value)
        node = Node(value)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = node
        node.next = temp
        self.size += 1
 
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return 'invalid index'
        if index == 0:
            temp = self.head
            self.head = temp.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return temp.value
        if index == self.size - 1:
            old_tail = self.tail
            new_tail = self.get(index - 1)
            self.tail = new_tail
            new_tail.next = None
            self.size -= 1
            return old_tail.value
        prev = self.get(index - 1)
        deleted_node = prev.next
        prev.next = deleted_node.next
        self.size -= 1
        return deleted_node.value