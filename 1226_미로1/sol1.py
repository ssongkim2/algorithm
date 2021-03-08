import sys
sys.stdin = open('input.txt')
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def solution(mem_row, mem_col):
    chk[mem_row][mem_col] = True
    if numbers[mem_row][mem_col] == 3:
        return True
    for i in range(4):
        row = mem_row +dr[i]
        col = mem_col +dr[i]
        if numbers[row][col] != 1:
            if chk[row][col] != True:
                solution(row, col)
def bfs(idx):


T = int(input())
for tc in range(1, 1+T):
    N = 16
    chk = [[False for _ in range(N)] for _ in range(N)]
    numbers = [[] for _ in range(N)]
    for idx in range(N):
        numbers[idx] = list(map(int,input()))
    print(solution(1,1))
    # print(numbers)