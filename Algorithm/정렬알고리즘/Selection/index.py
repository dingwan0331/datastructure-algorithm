# min 값 기반 selection sort

def selection_sort1(array:list) -> list:
    n = len(array)
    
    for i in range(n):
        min_num = min(array[i:])
        min_idx = array[i:].index(min_num)
        array[i], array[i+min_idx] = array[i+min_idx], array[i]

    return array

# max값 기반 selection sort

def selection_sort2(array:list) -> list:
    n = len(array)

    for i in range(n-1):
        last_idx = n-1-i
        max_num = max(array[:last_idx])
        max_idx = array.index(max_num)
        array[last_idx], array[max_idx] = array[max_idx], array[last_idx]
    return array

print(selection_sort1([1,5,16,26,27,1,11,1,1,1,1,2,2,2]))