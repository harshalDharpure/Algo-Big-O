def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

print(selection_sort([5,4,3,2,1])) # [1, 2, 3, 4, 5]