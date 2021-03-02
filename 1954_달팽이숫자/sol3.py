import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    number = [[0]*N for _ in range(N)]
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    idx = 0
    r = 0
    c = 0
    goal = N*N
    num = 1
    number[0][0] = 1

    while True:                    #idx 계속 돌리기
        nr = r+dr[idx]
        nc = c+dc[idx]
        if 0 <= nc < N and 0 <= nr < N and number[nc][nr] == 0:   #if문안에서 idx 0이 계속돌다가 0 <= nc < N and 0 <= nr <
            # N and number[nc][nr] == 0이 조건 만나면 else로 넘어가고 else에서 idx 컨트롤 그후 goal까지 num이 도달하면 시마이
            num += 1
            r = nr
            c = nc
            number[nc][nr] = num
        else :
            idx = (idx+1)%4

        if num == goal:
            break
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(number[i][j], end=' ')
        print()