import sys
sys.stdin = open('sample_input.txt')

def check(r, c):
    for i in range(8):
        cnt = 1
        nr = r +dr[i]                   #여기 똑바로 하는거 공부
        nc = c +dc[i]
        while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':  #이거는 한쪽방향이 맞으면 한쪽방향으로 계속 보내는것
            cnt += 1
            nr, nc = nr + dr[i], nc + dc[i]
        if cnt > 4:
            return True
    return False


T = int(input())
dr = [-1, 1, 0, 0, -1, 1, 1, -1]      #상하좌우 시계방향대각선
dc = [0, 0, -1, 1, 1, 1, -1, -1]
for tc in range(1,T+1):
    N = int(input())
    board = [input() for _ in range(N)]

    print(board)
    # flag = 0
    # for i in range(N):
    #     for j in range(N):
    #         if board[i][j] == '.':
    #             continue
    #         if check(i, j):
    #             flag = 1
    #             break
    #     if flag: break
    #     #함수를 안쓰고 for문 두개안에 있으니까 break가 두개있어야함