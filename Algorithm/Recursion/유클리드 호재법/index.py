def gcd(max_num, min_num):
    if max_num % min_num == 0:
        return min_num

    return gcd(min_num, max_num % min_num )