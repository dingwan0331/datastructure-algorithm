# Binary-Search(이진탐색)

## 구현코드

1. 반복문 형태
2. 재귀 형태

## 이진탐색이란?

정렬된 리스트에서 탐색 범위를 절반씩 줄여서 탐색하는방법  
시작점, 끝점, 중간점을 활용하여 범위를 설정합니다.  
일반적인 for 루프 (순차 탐색) 은 O(n)의 시간복잡도를 가지지만
이진탐색은 O(log n)의 시간복잡도를 가집니다.

## 순차탐색 vs 이진탐색

### 순차탐색

```
nums = [1,2,3,4,5,6,7]
n = len(nums)
target = 7

for i in range(n):
    if nums[i] == target:
        return i
```

이렇게 가장 마지막에 해당 target이 있다면 n번만큼 반복문을 순회하여야 합니다.
이는 시간복잡도 O(n)을 의미합니다.

### 이진탐색

```
nums = [1,2,3,4,5,6,7]
end = len(nums) - 1
start = 0
taget = 7

while start <= end:
    mid = (start + end) //2
    # 값을 찾을경우 현재 mid 인덱스 반환
    if nums[mid] == target:
        return mid
    # 값이 중간점의 값보다 작을때 end의 mid로 땡겨 탐색
    if nums[mid] > target:
        end = mid - 1
    # 값이 중간점의 값보다 클때 start를 mid로 땡겨 탐색
    if nums[mid] < target:
        start = mid + 1
```

한번의 while 문을 통과할때 마다 탐색 범위는 절반으로 줄어들기때문에
O(log n)의 시간복잡도를 보장할 수 있습니다.
mid에 +1 or -1을 하는 이유는 해당지점(mid)는 이미 탐색이 완료 되었기 때문입니다.

# 이진탐색의 단점

이진탐색의 단점이라고 하면 바로 해당 리스트가 정렬되어 있어야 한다는점 입니다.
