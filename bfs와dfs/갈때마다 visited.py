import sys
sys.stdin = open('input.txt')

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
    while stack:
        v = stack.pop()
        path += [v]

        adj_list[v].sort()
        adj_list[v].reverse()

        for w in adj_list[v]:
            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1

    print(' '.join(map(str, path)))