def sort_string(s:str) -> str:
    sum_number = 0
    result = []
    for i in s:
        if i.isalpha():
            result.append(i)
        else:
            sum_number += int(i)
    result.sort()
    return ''.join(result) + str(sum_number)