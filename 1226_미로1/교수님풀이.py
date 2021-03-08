import sys
sys.stdin = open('input.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
     Q = [(r,c)]

    while Q:
        cur_r, cur_c = Q.pop(0)
        #서있는 위치가 도착지점인가?
        for i in range(4):
            nr = cur_r+dr[i]
            nc = cur_c +dc[i]
            if nr<0 or nr>=N or nc<0or nc>=N:
                continue
            if maze[nr][nc] == 3 :
                return 1
            if maze[nr][nc] != 1:
                Q.append((nr,nc))
                maze[nr][nc] = 1
    return 0




for tc in range(10):
    tc_num = int(input())
    N = 16

    maze = [list(map(int,input())) for _ in range(N)]

    #시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j
                maze[i][j] = 1
