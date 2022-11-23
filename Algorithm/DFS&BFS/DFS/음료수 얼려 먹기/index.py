def cold(n,m, map_list):
    dx = (1,-1,0,0)
    dy = (0,0,-1,1)

    def dfs(x,y):
        if x < 0 or y < 0 or m <= x or n <= y:
            return
            
        if map_list[y][x] == 0:

            map_list[y][x] = 3
            for i in range(4):
                return dfs(x + dx[i],y + dy[i])

    answer = 0

    for i in range(n):
        for j in range(m):
            if map_list[i][j] == 0:
                map_list[i][j] = 3
                for k in range(4):
                    dfs(j + dx[k] , i + dy[k])
                print(map_list)
                answer += 1

    return answer