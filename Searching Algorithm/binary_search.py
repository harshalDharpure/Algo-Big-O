def binary_search(arry,target):
    left=0
    right=len(arry)-1

    while left<=right:
        middle=(left+right)//2
        if arry[middle] == target:
            return middle
        elif arry[middle] < target:
            left = middle +1
        else:
            right = middle -1
    return -1
print(binary_search([2,3,7,9,11,23,37,81,87,89],87))


##this is iterative Process
