import sys
sys.stdin = open('input.txt')

# T = int(input())
for tc in range(1,11):
    T= int(input())
    dr = [-1,1,0,0] #상하
    dc = [0,0,-1,1] #좌우
    nxt ='U'
    ladder = [0]*100
    for i in range(100):
        ladder[i] = list(map(int,input().split()))
    # print(ladder)

    for row in range(100):
        if ladder[99][row] == 2:
            mem = row
    # print(mem)
    ladder[99][mem]=1
    while row > 0 and 1<=col<=98:
        if
