import sys
sys.stdin = open('sample_input.txt')
dr = [-1,1,0,0]  #상하좌우
dc = [0,0,-1,1]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = [0]*N
    chk = [[False]*N for _ in range(N)]
    nr = 0
    nc = 0
    cur = N-1
    result = 0
    for idx in range(N):
        numbers[idx] = list(map(int,input()))
    for row in range(N):
        for col in range(N):
            if numbers[row][col] == 2:
                nr = row
                nc = col
    # while 0 <= nc < N and 0 <= nr < N:
    #     for i in range(4):
    #         mr = nr + dr[i]
    #         mc = nc + dc[i]
    #         if numbers[mr][mc] == 0 and chk[mr][mc] == False:
    #             chk[mr][mc] = True
    #             nr = mc
    #             nc = mc
    #         elif numbers[mr][mc] == 3:
    #             nr = mc
    #             nc = mc
    #             break
    #         else : continue
    for i in range(4)
        mc = nc + dc[i]
        mr = nr + dr[i]

        while 0<=mc<N and 0<=mc<N:
            if




        idx += 1
        if idx >= 4:
            idx = idx %4



    print(nr)
    print(nc)