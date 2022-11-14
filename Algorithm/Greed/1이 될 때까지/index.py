def make_one(n,k):
    count = 0
    while n !=1:
        # n이 나누어 떨어지면
        if n % k == 0:
            # 나누기
            n //= k
        else:
            # 그렇지 않다면 -1 하기
            n -= 1
        count += 1
    return count  

# log 시간복잡도를 가지는 solution
def solution_one(n,k):
    count = 0
    while n >= k:
        # n에서 가장가까운 (낮은수 중에)정수나누기가 가능한 수 찾기
        target = (n//k) * k
        # target(정수 나누기가 가능한 수) 까지 빼기 연산을 해야하기때문에 
        # n - target만큼 해주기 즉 - 연산 횟수를 세는 과정
        count += (n - target)

        # 1번의 나누기 연산후 연산횟수 증가시켜주기
        n //= k
        count += 1
    # 남은수는 더이상 나눠지지 않는 수 이기에 - 연산 횟수 세어주기
    count += (n-1)
    return count