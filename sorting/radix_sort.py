# Part 1: Code with Comments explaining Time Complexity

# Part 2: Code with Comments explaining Space Complexity

# Part 1 -

# Time Complexity: As there are n digits and each digit is run through counting sort (which takes O(n+k)), the time complexity is O(d*(n+k)). Since we are using decimal system, b is a constant, so we can simplify the time complexity to O(d*n).

def radix_sort(array):
    if len(array) == 0:
        return 'empty array'
 
    # Finding the max and the number of digits takes O(n)
    greatest_number = max(array)
    number_of_digits = len(str(greatest_number))
 
    # number of times counting sort needs to be done = digits in greatest number
    # For each digit, perform counting sort. This gives us O(d*(n+k))
    # where d is the number of digits, n is the number of elements, and k is the base (10 for decimal)
    for i in range(number_of_digits):
        counting_sort(array, i)
 
    return array
 
def counting_sort(array, place):
    output = [0] * len(array)
    temp = [0] * 10  # We're using base 10
    digit_place = 10 ** place
 
    # Counting occurrence of digits. This is O(n)
    for num in array:
        digit = (num // digit_place) % 10
        temp[digit] += 1
 
    # Calculate cumulative count. This is O(k), k is base here i.e., 10
    for i in range(1, 10):
        temp[i] += temp[i - 1]
 
    # Populate the output array. This is O(n)
    for j in range(len(array) - 1, -1, -1):
        curr_digit = (array[j] // digit_place) % 10
        temp[curr_digit] -= 1
        insert_position = temp[curr_digit]
        output[insert_position] = array[j]
 
    array[:] = output[:]
# Part 2-

# Space Complexity: The space complexity of Radix Sort is O(n+k),
# where n is the number of elements, and k is the base of the numbers 
# (10 for decimal numbers). In counting_sort, 
# we're creating two additional arrays, temp and output,
# of size n and k respectively. Therefore, the space complexity is O(n+k). 
# And this simplifies to O(n) in the case of decimal values

def radix_sort(array):
    # The space for array is O(n)
    if len(array) == 0:
        return 'empty array'
 
    greatest_number = max(array)
    number_of_digits = len(str(greatest_number))
 
    for i in range(number_of_digits):
        counting_sort(array, i)
 
    return array
 
def counting_sort(array, place):
    # The space for output and temp is O(n+k)
    output = [0] * len(array)
    temp = [0] * 10  # We're using base 10
    digit_place = 10 ** place
 
    for num in array:
        digit = (num // digit_place) % 10
        temp[digit] += 1
 
    for i in range(1, 10):
        temp[i] += temp[i - 1]
 
    for j in range(len(array) - 1, -1, -1):
        curr_digit = (array[j] // digit_place) % 10
        temp[curr_digit] -= 1
        insert_position = temp[curr_digit]
        output[insert_position] = array[j]
 
    array[:] = output[:]