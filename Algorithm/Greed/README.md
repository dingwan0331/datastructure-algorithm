# Greed(탐욕법)

- 현재 상황에서 지금 가장 좋은것을 고르는 알고리즘
- 일반적으로 문제를 풀기위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구한다.
- 정당성이 분석이 중요 (그리디 알고리즘으로 얻은 해가 최적의 해 인가?)
  - 가장 좋아보이는것을 반복적으로 선택해도 최적의 해를 구할 수 있는지가 중요하다.

# 그리디 알고리즘 예시

<img width="1071" alt="image" src="https://user-images.githubusercontent.com/100751719/201593237-9237b273-81e2-4c03-9f7d-eff207779bf0.png">
해당문제의 정답은 5 - 7 - 9를 선택하여야 한다 하지만 그리디 알고리즘은 매순간의 최적의 해를 구한다.
<img width="1071" alt="image" src="https://user-images.githubusercontent.com/100751719/201593429-276041c7-c925-4d69-a7d1-a22d1a0c43e1.png">
현재상황에서의 최적의 해(해당 그림은 자식노드중에서 가장 큰값)만 고르며 진행한다.
이것이 그리디 알고리즘이다.

# 정답이 아닌것같은데?!

일반적으로 그리디알고리즘은 최적의 해를 보장하지 않을때가 많습니다.

하지만 대부분의 코딩테스트에서는 그리디알고리즘을 사용한 해가 최적의 해가 될 경우로 출제하게 된다고 합니다.
