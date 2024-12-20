def bubble_Sort(array):
    started = False
    counter =0
    while not started:
        started = True
        for i in range(len(array)-1-counter):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
                started = False
        counter+=1
    return array
print(bubble_Sort([5,4,3,2,1]))