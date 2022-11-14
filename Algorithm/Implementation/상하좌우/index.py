def travle(n, plans):
    config = {
                'R': (1,0),
                'L': (-1,0),
                'U': (0,-1),
                'D': (0,1)
            }
    plans = list(map(lambda x : config[x],plans.split(' ')))
    x, y = 1, 1

    for plan in plans:
        nx, ny = x + plan[0],y + plan[1]
        if nx > n or nx < 0 or ny > n or ny <0:
            continue
        else:
            x, y = nx, ny
    return [x, y]