import sys
sys.stdin = open('input.txt')
def solution(F):
    N = F*F
    mat = [[0]*F for _ in range(F)]
    idx = 0
    row = 0
    col = 0
    num = 1
    nr = row + dr[idx]
    nc = col + dc[idx]
    mat[row][col] = 1
    while True:

        if 0<=nr<F and 0<=nc<F and mat[nc][nr]==0:
            nr = nr + dr[idx]
            nc = nc + dc[idx]
            num += 1
            mat[nr][nc] = num
        else:
            idx = (idx+1)/4
        if num == N:
            return mat
dr = [0,1,0,-1]
dc = [1,0,-1,0]

T = int(input())
for tc in range(1, T+1):
    F =int(input())
    print(solution(F))