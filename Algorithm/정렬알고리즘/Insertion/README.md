# Insertion Sort(삽입 정렬)

Insertion Sort는 Selection Sort와 유사하지만, 좀 더 효율적인 정렬 알고리즘이다.

Insertion Sort는 2번째 원소부터 시작하여 그 앞(왼쪽)의 원소들과 비교하여 삽입할 위치를 지정한 후, 원소를 뒤로 옮기고 지정된 자리에 자료를 삽입 하여 정렬하는 알고리즘이다.

최선의 경우 O(N)이라는 엄청나게 빠른 효율성을 가지고 있어, 다른 정렬 알고리즘의 일부로 사용될 만큼 좋은 정렬 알고리즘이다.

# 동작 과정

기본시작은 2번째 요소 부터 시작한다.

현재 요소보다 앞쪽 요소를 prev명명한다.

1. 현재 요소를 temp에 저장
2. prev와 prev+1을 비교하여 prev가 크면 prev 를 땡기고 prev를 -1하는 과정을 반복한다.
3. 2번 조건 미충족시 prev+1에 temp를 삽입한다.
4. 이를 배열끝까지 반복한다.

# 코드

```
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
```

# 시간복잡도

최악의 경우(역으로 정렬되어 있을 경우) Selection Sort와 마찬가지로, (n-1) + (n-2) + .... + 2 + 1 => n(n-1)/2 즉, O(n^2) 이다.

하지만, 모두 정렬이 되어있는 경우(Optimal)한 경우, 한번씩 밖에 비교를 안하므로 O(n) 의 시간복잡도를 가지게 된다.

또한, 이미 정렬되어 있는 배열에 자료를 하나씩 삽입/제거하는 경우에는, 현실적으로 최고의 정렬 알고리즘이 되는데, 탐색을 제외한 오버헤드가 매우 적기 때문이다.

최선의 경우는 O(n) 의 시간복잡도를 갖고, 평균과 최악의 경우 O(n^2) 의 시간복잡도를 갖게 된

# 공간복잡도

주어진 배열 안에서 교환(swap)을 통해, 정렬이 수행되므로 O(n) 이다.

# 장점

알고리즘이 단순하다.

대부분의 원소가 이미 정렬되어 있는 경우, 매우 효율적일 수 있다.

정렬하고자 하는 배열 안에서 교환하는 방식이므로, 다른 메모리 공간을 필요로 하지 않는다. => 제자리 정렬(in-place sorting)

안정 정렬(Stable Sort) 이다.

Selection Sort나 Bubble Sort과 같은 O(n^2) 알고리즘에 비교하여 상대적으로 빠르다.

# 단점

평균과 최악의 시간복잡도가 O(n^2)으로 비효율적이다.

Bubble Sort와 Selection Sort와 마찬가지로, 배열의 길이가 길어질수록 비효율적이다.
