# DFS - Depth First Search (깊이 우선 탐색)

깊은부분(먼곳)을 먼저 탐색하는 탐색 방법을 의미합니다.

## 구현코드

1. Stack 형태
2. 재귀 형태

재귀도 call stack을 이용한 방식이기에 결국 stack방식을 취한다고 볼 수 있습니다.

## 코드 풀이시 사용할 자료구조

풀이를 위해 3가지의 list가 필요합니다.

1. 실제 방문을 기록할 list : log
2. 문제풀이를 위한 stack자료구조 : stack
3. 방문 여부를 기억할 list : visited

## 코드풀이 방식

1. 시작점을 stack에 넣고 방문처리 합니다.
2. 스택의 최상단과 인접한 노드를 stack에 넣고 방문처리합니다.
   - 이때 인접한 노드가 여러개일 시 작은것을 우선적으로 방문합니다.
3. 인접한 노드중 방문하지 않은 노드가 없다면 stack에서 제거 해줍니다.

- 방문처리한다 == visited의 해당index를 True로 하고 log에 append()해줍니다.
