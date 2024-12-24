class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
 
class PriorityQueue:
    def __init__(self):
        self.data = []
 
    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.data.append(node)
        self.bubble_up()
        return self
 
    def bubble_up(self):
        idx = len(self.data) - 1
        element = self.data[idx]
        while idx > 0:
            parent_idx = (idx - 1) // 2
            parent = self.data[parent_idx]
            if element.priority >= parent.priority:
                break
            self.data[idx] = parent
            self.data[parent_idx] = element
            idx = parent_idx
        # Time complexity: O(logn) as in worst case, we may have to traverse up to the root from the last node
        # The height of a binary heap is logn, hence the time complexity
 
    def dequeue(self):
        min_element = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.bubble_down()
        return min_element
 
    def bubble_down(self):
        idx = 0
        length = len(self.data)
        element = self.data[0]
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            left_child, right_child = None, None
            smallest = None
            if left_child_idx < length:
                left_child = self.data[left_child_idx]
                if left_child.priority < element.priority:
                    smallest = left_child_idx
            if right_child_idx < length:
                right_child = self.data[right_child_idx]
                if (smallest is None and right_child.priority < element.priority) or (
                        smallest is not None and right_child.priority < left_child.priority):
                    smallest = right_child_idx
            if smallest is None:
                break
            self.data[idx] = self.data[smallest]
            self.data[smallest] = element
            idx = smallest
        # Time complexity: O(logn) as in worst case, we may have to traverse from the root to the leaf node
        # The height of a binary heap is logn, hence the time complexity
 
# Space complexity: O(1) 