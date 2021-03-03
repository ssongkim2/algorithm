import sys
sys.stdin = open('dfs_bfs_input.txt')

def bfs(graph,start):
    queue = [start]
    path = []
    chk = [False for _ in range(N+1)]            #일단 큐에 들억나것 True
    while queue:
        current = queue.pop(0)                   #bfs와 dfs의 차이는 앞에서 찾아가냐 뒤에서 찾아가냐
        if chk[current] != True:
            queue += graph[current]
            chk[current] = True
            path.append(current)


    return path

    pass
T = int(input())
for tc in range(1,T+1):
    N, M, start = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        K, L = map(int,input().split())
        graph[K].append(L)
        graph[L].append(K)
    print(bfs(graph, start))