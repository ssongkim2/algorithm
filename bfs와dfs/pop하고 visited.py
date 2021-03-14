import sys
sys.stdin = open('input.txt')

def dfs(s):
    path = []
    visited = [0 for _ in range(V+1)]
    stack = [s]
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            path += [v]

        for i in matrix[v]:
            if matrix[v][i] == 1:
                if visited[i] == 0:
                    stack.append(i)
    return ' '.join(map(str, path))



for tc in range(1, 2):
    V, E, S = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        matrix[start][end] = 1
        matrix[end][start] = 1

    print(dfs(S))