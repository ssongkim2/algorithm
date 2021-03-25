import sys
sys.stdin = open('sample_input.txt')

#이거 bfs

def solution(row,col):
    queue = [numbers[row][col]]
    distance = [[0]*M for _ in range(N)]
    global H
    cnt = 0
    nr = row
    nc = col
    rear = 0
    distance[row][col] = 1
    while True: #마지막에 cnt 더함
        for idx in directions[queue[rear]]:
            flag = (idx+2)%4
            t = distance[nr][nc]
            if idx == 0 and nr - 1 >= 0:
                nr = nr - 1
                nc = nc
                if flag in directions[numbers[nr][nc]] and distance[nr][nc] == 0:
                    queue.append(numbers[nr][nc])
                    distance[nr][nc] = t + 1
                    if distance[nr][nc] == H+2:
                        return distance
            elif idx == 1 and nc + 1 < M:
                nr = nr
                nc = nc + 1
                if flag in directions[numbers[nr][nc]] and distance[nr][nc] == 0:
                    queue.append(numbers[nr][nc])
                    distance[nr][nc] = t + 1
                    if distance[nr][nc] == H+2:
                        return distance
            elif idx == 2 and nr + 1 < N:
                nr = nr + 1
                nc = nc
                if flag in directions[numbers[nr][nc]] and distance[nr][nc] == 0:
                    queue.append(numbers[nr][nc])
                    distance[nr][nc] = t + 1
                    if distance[nr][nc] == H+2:
                        return distance
            elif idx == 3 and nc - 1 >= 0:
                nr = nr
                nc = nc - 1
                if flag in directions[numbers[nr][nc]] and distance[nr][nc] == 0:
                    queue.append(numbers[nr][nc])
                    distance[nr][nc] = t + 1
                    if distance[nr][nc] == H+2:
                        return distance
        rear += 1
    return distance

T = int(input())
for tc in range(1, 1+T):
    N, M, R, C, H = map(int,input().split())
    #N은 세로 M은 가로 R은 세로 시작위치 C는 가로시작위치, H는 시간
    numbers=[0]*N
    distance = [[0] * M for _ in range(N)]
    for idx in range(N):
        numbers[idx] = list(map(int,input().split()))
    directions = [[], [0,1,2,3], [0,2], [1,3], [0,1], [1,2], [2,3], [0,3]]
    solution(R, C)