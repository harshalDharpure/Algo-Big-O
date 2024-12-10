def binary_search_recursive(nums,target):
    def helper(nums,target,left,right):
        if left>right: return -1
        middle = (left + right)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            return helper(nums,target,middle+1,right)
        else:
            return helper(nums,target,left,middle-1)
    return helper(nums,target,0,len(nums)-1)


print(binary_search_recursive([2,3,7,9,11,23,37,81,87,89],9))