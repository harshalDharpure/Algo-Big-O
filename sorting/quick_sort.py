# Part 1: Code with comments explaining Time complexity ( Optimum solution of Recursively calling Quick Sort on lower sized subarray)

# Part 2: Code with comments explaining Space complexity ( Optimum solution of Recursively calling Quick Sort on lower sized subarray)



# Quick Sort - Recursively QS lower sized 
# middle - pivot
#So, Quick Sort's best case time complexity is O(n log n) and worst case is O(n^2)
 
def swap(array, i, j):
    # This operation is O(1)
    array[i], array[j] = array[j], array[i]
 
def partition(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
 
    # Finding middle takes O(1)
    middle = (start + end) // 2
    swap(array, start, middle)
 
    pivot = array[start]
    i = start + 1
    j = end
 
    while i <= j:
        # In worst case scenario, this can take O(n)
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i < j:
            # This swap is O(1)
            swap(array, i, j)
 
    # This swap is O(1)
    swap(array, start, j)
    return j
 
def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
 
    while start < end:
        pivot_idx = partition(array, start, end)
 
        # Recursively call Quick Sort on lower sized subarray
        # Each recursion takes O(log(n)) in best case scenario and O(n) in worst case
        if pivot_idx - start < end - pivot_idx:
            quick_sort(array, start, pivot_idx - 1)
            start = pivot_idx + 1
        else:
            quick_sort(array, pivot_idx + 1, end)
            end = pivot_idx - 1
# Part 2-

# Quick Sort - Recursively QS lower sized 
# middle - pivot
#space complexity is O(log n) 
 
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]  # Space Complexity: O(1)
 
def partition(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
 
    middle = (start + end) // 2
    swap(array, start, middle)
 
    pivot = array[start]
    i = start + 1
    j = end
 
    while i <= j:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i < j:
            swap(array, i, j)
    swap(array, start, j)
 
    # i, j, pivot, start, end take constant space
    return j
 
def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
 
    while start < end:
        pivot_idx = partition(array, start, end)
 
        # Recursively call Quick Sort on lower sized subarray
        # The maximum depth of the recursion is log(n) because we are always 
        # recursing into the smaller part of the partition. Hence, the auxiliary 
        # space used is O(log(n)) even in the worst case.
        if pivot_idx - start < end - pivot_idx:
            quick_sort(array, start, pivot_idx - 1)
            start = pivot_idx + 1
        else:
            quick_sort(array, pivot_idx + 1, end)
            end = pivot_idx - 1