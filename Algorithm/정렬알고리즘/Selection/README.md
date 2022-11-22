# Selection Sort(선택 정렬)

O(n\*\*2)의 시간복잡도를 가지는 기초적인 정렬 알고리즘
코드는 단순하지만 높은 시간복잡도를 가진다.

# 동작방식

1. 주어진 리스트 중에 최소값을 찾는다.
2. 그 값을 맨 앞에 위치한 값과 교체한다.
3. 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.

반대로 최대값을 찾아 마지막 인덱스에 배치하는 방법도 가능하다.

# 슈도 코드

```
def selection_sort(array):
    n = len(array)
    for i in range(n):
        # 최솟값의 인덱스 찾기
        min_idx = min(array)의 index
        # 현재위치와 최솟값위치를 맞교환
        array[min_idx], array[i] = array[i], array[min_idx]
    return array
```
