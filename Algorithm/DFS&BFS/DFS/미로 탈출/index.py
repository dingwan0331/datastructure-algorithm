n, m = map(int, input().split(' '))
graph = [(list(map(int,input())))for i in range(n)]

def mirror(n,m,graph):
    visited = [[False for j in range(m)]for i in range(n)]
    dx = (1,-1,0,0)
    dy = (0,0,-1,1)
    visited[0][0] = True

    def dfs(x,y,value):
        # print(nx,ny)
        if x < 0 or y < 0 or m <= x or n <= y:
            return
    
        if graph[y][x] and not visited[y][x]:
            graph[y][x] += value
            visited[y][x] = True
            value = graph[y][x]
            for i in range(4):
                dfs(x + dx[i], y + dy[i],value)
    
    dfs(0,0,graph[0][0])
    print(graph)

    return graph[n-1][m-1]

print(mirror(n,m,graph))