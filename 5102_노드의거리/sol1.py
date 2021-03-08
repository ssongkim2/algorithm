import sys
sys.stdin = open('sample_input.txt')



def bfs(graph, start, end):
    queue = [start]
    chk = [False for _ in range(N+1)]
    while queue:
        current = queue.pop(0)
        if chk[current] != True:
            chk[current] = True
            queue += graph[current]
        if end == current:
            return distance[current]
        for i in graph[current]:
            if chk[i] != True:
                distance[i] = distance[current] + 1
    return 0

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int,input().split())
    graph = [[]for _ in range(N+1)]
    distance = [0]*(N+1)
    for _ in range(M):
        V, E = map(int, input().split())
        graph[E].append(V)
        graph[V].append(E)
    start, end = map(int, input().split())
    visited = [False for _ in range(N+1)]
    print('#{} {}'.format(tc,bfs(graph,start,end)))