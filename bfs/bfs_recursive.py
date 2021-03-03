def solution(idx):
    visited[idx] = True
    for i in graph[idx]:
        if visited[i] != True:
            visited[i] = True

            solution(i)
    return int(visited[G])