class MaxBinaryHeap:
    def __init__(self):
        self.heap = []
 
    def buildHeap(self, array):
        length = len(array)
        last_parent_index = length // 2 - 1
        for i in range(last_parent_index, -1, -1):  # From last parent to root
            self.bubbleDown(array, i)
        self.heap = array
        return self
 
    def bubbleDown(self, array, idx):
        length = len(array)
        current = array[idx]
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            largest = None
            # If left child exists
            if left_child_idx < length:
                left_child = array[left_child_idx]
                # If it's larger than current element, it could be the largest
                if left_child > current:
                    largest = left_child_idx
 
            # If right child exists
            if right_child_idx < length:
                right_child = array[right_child_idx]
                # If right child is larger than current and left child, it's the largest
                if (largest is None and right_child > current) or (largest is not None and right_child > array[largest]):
                    largest = right_child_idx
 
            # If there's no larger child, stop the loop
            if largest is None:
                break
            else:  # Swap current element with the largest child
                array[idx], array[largest] = array[largest], array[idx]
                idx = largest
 
    def extractMax(self):
        max_value = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last
            self.bubbleDown(self.heap, 0)
        return max_value
 
    def insert(self, value):
        self.heap.append(value)
        self.bubbleUp()
        return self
 
    def bubbleUp(self):
        idx = len(self.heap) - 1
        value = self.heap[idx]
        while idx > 0:  # Until we reach the root
            parent_idx = (idx - 1) // 2
            parent_value = self.heap[parent_idx]
            if value <= parent_value:
                break
            # Swap parent with current value
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx
 
    def peek(self):
        return self.heap[0]
 
 
# Test the heap
heap = MaxBinaryHeap()
heap.buildHeap([4,7,3,0,9,3,2,6])