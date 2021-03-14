from collections import deque


#dfs는 리턴값없이 visited만 바꾼다고 생각!

def dfs(graph, idx, visited):
    visited[idx] = True
    for i in graph[idx]:
        if visited[i] != True:
            dfs(graph, i, visited)
    return visited


visited = [False]*10
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

print(dfs(graph,4,visited))










