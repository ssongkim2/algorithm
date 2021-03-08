import sys
sys.stdin = open('sample_input.txt')
T = int(input())
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def solution(mem_row, mem_col):
    chk[mem_row][mem_col] = True
    global cnt
    cnt += 1
    if numbers[mem_row][mem_col] == 3:
        print(cnt-1)
    for i in range(4):
        row = mem_row + dr[i]
        col = mem_col + dc[i]
        if 0 <= row < N and 0 <= col < N:
            if numbers[row][col] != 1:
                if chk[row][col] != True:
                    solution(row, col)
    return
for tc in range(1, 1+T):
    N = int(input())
    chk = [[False for _ in range(N)]for _ in range(N)]
    cnt = 0
    numbers = [[] for _ in range(N)]
    for idx in range(N):
        numbers[idx] = list(map(int,input()))
    # print(numbers)
    mem_row = 0
    mem_col = 0
    for row in range(N):
        for col in range(N):
            if numbers[row][col] == 2:
                mem_row = row
                mem_col = col
    # if result == None:
    #     result = 0


    print(solution(mem_row,mem_col))