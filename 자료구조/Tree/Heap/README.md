## Tree란?

자료구조의 데이터 저장형태가 나무처럼 형성된 자료 구조

시작점을 의미하는 Root노드에서 아래로 나무 가지 처럼 뻗아나가는 구조입니다.

가지를 치는 규칙에 따라 다양한 종류의 Tree가 정의됩니다.

## Tree자료구조 종류

- binary search tree (이진검색트리)

- heap tree

  - max heap, min heap으로도 나뉩니다.

- balance tree(균형 이진 트리)

  - B-tree로 표현되며 MySQL의 인덱스 자료구조로 유명합니다.

- red-balck tree

- BinaryTree(이진트리)
  - 자식노드가 최대 2개인 트리 자료구조를 말합니다.

## Tree에서 사용되는 용어들

<img width="846" alt="image" src="https://user-images.githubusercontent.com/100751719/194826465-ce105393-3b75-4793-986f-63089c678acb.png">

- Root(Root Node): 부모가 없는 최상위 노드, 일반적으로 Tree 자료구조의 시작점
- Level: 트리에서 같은 깊이를 가지는 노드의 집합
- Depth: 루트에서 특정 노드까지의 경로의 개수(일반적으로 level과 동일합니다)
- Height: 이름 그대로 트리의 높이 루트에서 가장 끝의 leaf Node까지의 길이
- Parent Node: 어떤 특정노드의 상위노드
- Child Node: 어떤 특정노드의 하위 노드
- Sibling Node: 어떤 특정노드와 같은 level의 노드
- Leaf Node: Tree의 가장 끝 부분에 있는노드, 즉 자식이 없는 노드
- Sub Tree: Tree의 속해있는 하위트리. 하위 노드가아닌 하위 노드를 루트로 하는 트리를 의미

## BinaryTree 자료구조 표현법 3가지

<img width="407" alt="image" src="https://user-images.githubusercontent.com/100751719/194828497-81c094a6-9c6c-486e-b53e-2f990e9a63a2.png">

<br>

### 1. list표현법

level 0부터 위에서 아래로 왼쪽에서 오른쪽으로 순차적으로 리스트에 Insert한다

값이 없더라도 None으로 처리한다

위에 예제 사진을 list로 표현하면 다음과같다

```
[A, B, C, D, E, F, G, H, I, J, None, None, None, None, None]
```

만약 예제사진에서 G노드가 없다면?

```
[A, B, C, D, E, F, None, H, I, J, None, None, None, None, None]
```

상위노드가 없더라도 모두 None으로 처리하여 표현한다
<br><br>

### 2. 다차원 list표현법

부모노드와 노드와 자식 2개의 노드를 1개의 리스트로 표현한다 <br>
자식이 공백인경우는 빈 list로 표현한다.

ex) Root Node가 2이고 왼쪽자식이 1 오른쪽 자식이 2인경우 아래와 같이 표현할 수 있다.

```
[2,
  [
    1,[],[]
  ],
  [
    3,[],[]
  ]
]
```

예제 사진 표현해보기

```
[
  A,[
    B,[
      D,[
        H,[],[]
      ],
      [
        I,[],[]
      ]
.....
      ]
    ]
  ]
]
```

굉장히 복잡하고 길게 형성이됩니다.<br>

### 3.클래스 표현법

```
class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.parents = None
        self.left = None
        self.right = None
```

Node는 트리중 하나의 구성요소를 의미합니다.

parents는 상위노드 or 부모노드를 의미합니다.

left는 왼쪽 자식노드, right는 오른쪽 자식 노드를 의미합니다.
