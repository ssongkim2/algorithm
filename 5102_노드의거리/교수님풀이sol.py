import sys
sys.stdin = open('sample_input.txt')

def BFS(start):
    Q = [[start,0]]                    #큐를 생성과 동시에 안에 리스트를 선언
    visited = [False] * (V+1)
    visited [start] = True
    while Q:
        V, distance = Q.pop(0)
        if V == end:
            return distance
        for i in range(1, V+1):
            if adj_arr[V][i] == 1 and visited[i] == False:          #인접행렬의 V행을 다 보면서 연결되어있고 방문하지 않았는지 판별!
                Q.append([i, dist+1])
                visited[i] = True
    return 0

def BFS2(start):
    Q = [start]                    #큐를 생성과 동시에 안에 리스트를 선언
    visited = [False] * (V+1)
    visited [start] = True
    distance = 0
    while Q:
        size =len(Q)                  #사이즈를 한시점에 묶어서 돌리지 않으면 큐에서 빠지면서 사이즈가 바뀜 그래서 고정시켜줘야함
        for i in range(size):

            V = Q.pop(0)
            if V == end:
                return distance
            for i in range(1,V+1):
                if not visited[i] and adj_arr[V][i]:
                    Q.append(i)
                    visited[i] = True
        distance += 1
    return 0


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    #인접행렬을 이용하여 작성
    adj_arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        #무방향이므로 양쪽 연결
        adj_arr[a][b] = 1
        adj_arr[b][a] = 1
    #시작점, 끝점
    start , end = map(int,input().split())