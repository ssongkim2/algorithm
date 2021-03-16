import sys
sys.stdin = open('sample_input.txt')

#이거 dfs인듯

def solution(row,col):
    distance[row][col] = 1
    H = H-1
    if H == 0:
        return
    else:
        if numbers[row][col] != 0:
            if numbers[row][col] == 1:
                if row - 1 >= 0:
                    if solution:



T = int(input())
for tc in range(1, 1+T):
    N, M, R, C, H = map(int,input().split())
    #N은 세로 M은 가로 R은 세로 시작위치 C는 가로시작위치, H는 시간
    numbers=[0]*N
    distance = [[0] * M for _ in range(N)]
    for idx in range(N):
        numbers[idx] = list(map(int,input().split()))
    solution(R, C)