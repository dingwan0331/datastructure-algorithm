from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                answer.append(i)
                queue.append(i)
                visited[i] = True

start = 1

answer = [start]

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

bfs(graph, start, visited)
print(answer)