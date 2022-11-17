def gcd(a,b):
    min_num, max_num = min(a,b), max(a,b)

    if max_num % min_num == 0:
        return max_num
    return gcd(min_num, max_num % min_num )

print(gcd(11,10))