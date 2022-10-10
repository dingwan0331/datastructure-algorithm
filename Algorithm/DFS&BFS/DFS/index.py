stack = []
answer = []

def dfs(graph, v, visited):
    # 해당 노드를 방문처리
    visited[v] = True
    answer.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return answer

# 시작위치
v = 1

# 노드들의 연결된 그래프 (2차원리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * len(graph)

print(dfs(graph,v,visited))