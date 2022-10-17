# Heap 이란?

우선순위 큐를 위해 만들어진 자료구조이다.
<br>
여러 개의 값 중에서 가장 크거나 작은 값을 빠르게 찾기 위해 만든 이진 트리

- Root노드가 최대값인 힙 = 최대힙, max heap
- Root노드가 최소값인 힙 = 최소힙, min heap

(이글은 max heap을 기준으로 합니다.)

# Heap의 특징

1. 루트노드는 가장 큰 값이 들어 있습니다.
2. 중복값을 허용합니다.
3. 최대값을 O(1)시간내에 읽기, 삭제 연산을 제공합니다.

# Heap의 조건

1. 완전이진트리 형태를 띄어야 한다.
2. 부모노드는 자식노드보다 작거나 같아야 합니다.

# Heap의 관계노드 구하는법

## 부모노드

H = Heap 배열

k = 본인의 index

```
H[ (k - 1) // 2 ]
```

## 자식노드

왼쪽

```
H[ 2 * k + 1]
```

오른족

```
H[ 2 * k + 2]
```

# 무작위 배열에서 Heap만들기

## make-heap

마지막 인덱스부터 루트 인덱스 까지 반복하면서 heapify-down을 반복하는것

```
# 슈도 코드
def make_heap(A):
    n = len(A)
    for i in range(n-1,-1,-1):
        #A[k] = heap성질을 만족하는 곳
        heapify_down(A,k,n)
```

## heapify-down

해당 노드와 두개의 자식노드를 하나의 트리로 하여 heap성질을 만족시키는 연산

```
# 슈도 코드
def heapify_down(A,k,n):
    while A[k] != reaf_node:
        m = max_index(A[k], A[R], A[L])
        if A[k] != m:
            A[k] <-> A[m]
        else:
            break
```

노드가 리프노드이거나 혹은 heap성질을 만족할때까지 반복

## 본 코드에서 제공하는 연산

1. insert
   - O(log n)
2. find_max
   - O(n)
3. delete_max
   - O(log n)
4. make_haep
5. heapify_down
