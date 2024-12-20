def merge_sort(array1,array2):
    i = 0
    j = 0
    result = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1
    result += array1[i:]
    result += array2[j:]
    return result

print(merge_sort([1,3,5],[2,4,6])) # [1, 2, 3, 4, 5, 6]