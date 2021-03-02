import sys
sys.stdin = open('sample_input(1).txt')
dr = [-1,1,1,-1]
dc = [1,1,-1,-1]     #시계방향
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    board = [[0] * N for _ in range(N)]
    board[N//2-1][N//2-1] = 2  # 2가 백돌
    board[N//2][N//2] = 2
    board[N//2-1][N//2] = 1  # 1이 흑돌 초기값
    board[N//2][N//2-1] = 1
    for _ in range(M):
        c, r, color = map(int,input().split())
            #c,r 1씩 빼줘야함
        board[r-1][c-1] = color
            # 가로검사
        # x = r-1
        for col in range(N):
            if board[r-1][col] == color:
                if c-1 < col:
                    for col2 in range(c-1, col):
                        board[r-1][col2] = color
                else:
                    for col2 in range(col,c-1):
                        board[r-1][col2] = color
            #세로검사
        # col = c-1
        for row in range(N):
            if board[row][c-1] == color:
                if r-1 < row:
                    for row2 in range(r-1,row):
                        board[row2][c-1] = color
                else:
                    for row2 in range(row,r-1):
                        board[row2][c-1] = color
            #증가대각선검사
        nc = 0
        nr = 0
        while 0 <= nc < N and 0 <= nr < N:
            nr,nc = r+dr[0], c+dc[0]
            if board[r-1][c-1] and board[nr][nc] == color:
                idx = 0
                while idx<nr-r-1:
                    idx += 1
                    board[r-1-idx][c-1+idx] = color
                break
        while 0 <= nc < N and 0 <= nr < N:
            nr,nc = r+dr[1], c+dc[1]
            if board[r-1][c-1] and board[nr][nc] == color:
                idx = 0
                while idx<nr-r-1:
                    idx += 1
                    board[r-1+idx][c-1+idx] = color
                break
        while 0 <= nc < N and 0 <= nr < N:
            nr,nc = r+dr[2], c+dc[2]
            if board[r-1][c-1] and board[nr][nc] == color:
                idx = 0
                while idx<nr-r-1:
                    idx += 1
                    board[r-1+idx][c-1-idx] = color
                break
        while 0 <= nc < N and 0 <= nr < N:
            nr,nc = r+dr[3], c+dc[3]
            if board[r-1][c-1] and board[nr][nc] == color:
                idx = 0
                while idx < nr-r-1:
                    idx += 1
                    board[r-1-idx][c-1-idx] = color
                break






        # if r > c:
        #     idx = 0
        #     idx2 = 0
        #     while idx < N - r - 1:
        #         idx += 1
        #         if board[r-1+idx][c-1+idx] == color:
        #             for idx2 in range(idx):
        #                 board[row+idx2][col+idx2] = color
        #     while N-idx2-r-1>0
        #
        # elif r < c:
        #     idx = 0
        #     idx2 = 0
        #     while idx < N - c - 1:
        #         idx += 1
        #         if board[r-1+idx][c-1+idx] == color:
        #             for idx3 in range(idx):
        #                 board[row+idx3][col+idx3] = color
        #     while r-idx2-1>0:
        #         idx2+=1
        #         if board[r-1+idx2][c-1-idx2] == color:
        #             for idx4 in range(idx2):










        # while 0 <= r-1 < N and 0 <= c-1 < N:  #이거는 한쪽방향이 맞으면 한쪽방향으로 계속 보내는것
        #     nr, nc = nr + dr[0], nc + dc[0]
        #     if board[r-1][c-1] and  board[nr][nc] == color:
        #         for idx in range(nc-c-1):
        #             board[r-1+idx][c-1+idx] = color
        # while 0 <= r-1 < N and 0 <= c-1 < N:  #이거는 한쪽방향이 맞으면 한쪽방향으로 계속 보내는것
        #     nr, nc = nr + dr[1], nc + dc[1]
        #     if board[r-1][c-1] and  board[nr][nc] == color:
        #         for idx in range(nc-c-1):
        #             board[r-1+idx][c-1+idx] = color



    print(board)





























        # if r > c:
        #     idx = 0
        #     idx2 = 0
        #     while idx < N - r - 1:
        #         idx += 1
        #         if board[r-1+idx][c-1+idx] == color:
        #             for idx2 in range(idx):
        #                 board[row+idx2][col+idx2] = color
        #     while N-idx2-r-1>0
        #
        #
        # elif r < c:
        #     idx = 0
        #     idx2 = 0
        #     while idx < N - c - 1:
        #         idx += 1
        #         if board[r-1+idx][c-1+idx] == color:
        #             for idx3 in range(idx):
        #                 board[row+idx3][col+idx3] = color
        #     while r-idx2-1>0:
        #         idx2+=1
        #         if board[r-1+idx2][c-1-idx2] == color:
        #             for idx4 in range(idx2):
        #
        #
        #     #감소대각선 검사


            # for row in range(M):
            #     for col in range(M):
            #         for






