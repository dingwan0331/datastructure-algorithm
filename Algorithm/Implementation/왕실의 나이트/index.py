def night(d):
    N = 8
    # 아스키코드에 -96 을 해주면 'a'를 기준으로 1이 된다.
    x, y = ord(d[0]) - 96, int(d[1])
    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]

    result = 0
    
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 1 or N < nx or ny < 1 or N < ny:
            continue
        result += 1 

    return result