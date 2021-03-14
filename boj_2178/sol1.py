import sys
sys.stdin = open('input.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]   #상하좌우

def sol(N,M):
    visited = [[False]*M for _ in range(N)]
    distance = [[0]*M for _ in range(N)]
    visited[0][0] = True
    Q = [0]*1000000
    front = -1
    rear = 0
    Q[rear] = (0,0)
    while front != rear:
        front += 1
        cur_row, cur_col = Q[front]
        if cur_row == N-1 and cur_col == M-1:
            return distance[N-1][M-1]+1
        for i in range(4):
            nr = cur_row + dr[i]
            nc = cur_col + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if numbers[nr][nc] == 1 and visited[nr][nc] == False:
                    rear += 1
                    visited[nr][nc] = True
                    distance[nr][nc] = distance[cur_row][cur_col]+1
                    Q[rear] = (nr,nc)
    return 0



N, M = map(int,input().split())
numbers = [0]*N
for idx in range(N):
    numbers[idx] = list(map(int,input()))
print(sol(N,M))
