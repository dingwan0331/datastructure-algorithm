def insertion_sort(array):
    n = len(array)

    for i in range(1,n):
        temp = array[i]
        prev = i-1
        while prev >= 0 and array[prev] > temp:
            array[prev + 1] = array[prev]
            prev -= 1
        array[prev+1] = temp
    return array