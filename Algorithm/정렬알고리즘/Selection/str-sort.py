# 오름차순 정렬
def str_selection_sort(string:str) -> str:
    n = len(string)
    str_list = list(map(ord,string))

    for i in range(n-1):
        max_idx = str_list.index(max(str_list[:n-1-i]))
        str_list[n -1 -i],str_list[max_idx] = str_list[max_idx], str_list[n-1-i]

    return ''.join(list(map(chr,str_list)))

# 내림차순 정렬
def str_selection_sort_desc(string:str)->str:
    n = len(string)
    str_list = list(map(ord,string))

    for i in range(n-1):
        min_idx = str_list.index(min(str_list[:n-1-i]))
        str_list[n -1 -i],str_list[min_idx] = str_list[min_idx], str_list[n-1-i]
        
    return ''.join(list(map(chr,str_list)))