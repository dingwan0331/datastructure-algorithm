def find_charge(N):
    # 점원이 가지고 있는 거스름돈의 종류
    COINS = [500,100,50,10]

    count_coin = 0

    for coin in COINS:
        # 각 동전별 갯수 구하기
        count_coin += N // coin
        # 돌려줘야하는 거스름돈에서 돌려준 만큼 뺀 나머지 구하기
        N %= coin
    return count_coin