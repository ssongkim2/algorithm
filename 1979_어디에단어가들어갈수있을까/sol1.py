import sys
# from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N,K = map(int,input().split())

    puzzle = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):

        cnt = 0
        #행을 검사
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] or j == N-1 :
                #벽을 만났을 때 그동안 쌓아온 cnt값이 k이면 들어갈수 잇다
                if cnt == K:
                    ans += 1 
                cnt = 0

        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

