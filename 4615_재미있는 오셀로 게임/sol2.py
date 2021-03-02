import sys
sys.stdin = open('sample_input(1).txt')
dr = [-1,0,1]
dc = [-1,0,1]     #이거 이중으로 돌려서 9가지 방향을 나타낼거임
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N//2-1][N//2-1] = 2  # 2가 백돌
    board[N//2][N//2] = 2
    board[N//2-1][N//2] = 1  # 1이 흑돌 초기값
    board[N//2][N//2-1] = 1
    cnt1 = 0
    cnt2 = 0
    for _ in range(M):
        X, Y, color = map(int, input().split())
        A = X-1
        B = Y-1

        board[B][A] = color
        for row in dr:
            for col in dc:
                if row == col == 0:      #제자리인 경우 제외
                    continue
                else:
                    nr = B + row
                    nc = A + col
                    flag = False
                    while 0 <= nr < N and 0 <= nc < N:                   #이 인덱스가 중요함!!! 이거 디버깅 해보기1!!
                        if board[nr][nc] == 3 - board[B][A]:             #서로 다른색
                            nr = nr + row
                            nc = nc + col
                        elif board[nr][nc] == board[B][A]:
                            flag = True
                            break
                        else:                                           #0이라면
                            break
                    if flag:                                           #있으면
                        # px, py 는 이동할 때 쓸 idx
                        mr = B + row
                        mc = A + col
                        while mr != nr or mc != nc:
                            board[mr][mc] = color
                            mr = mr + row
                            mc = mc + col

    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                cnt1 += 1
            elif board[row][col] == 2:
                cnt2 += 1

    print('#{} {} {}'.format(tc,cnt1,cnt2))



