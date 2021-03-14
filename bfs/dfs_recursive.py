import sys
sys.stdin = open('input.txt')

def dfs(idx):
    visited[idx] = True
    print(idx, end=' ')
    for i in adj_list[idx]:
        if visited[i] == False:
            dfs(i)

for tc in range(1,2):
    V, E, S = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)
    # print(adj_list)

    path = []
    visited = [0 for _ in range(V+1)]
    visited[S] = 1
    stack = [S]
    print(dfs(1))