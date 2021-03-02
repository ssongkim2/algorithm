import sys
sys.stdin = open('input.txt')

# T = int(input())
for tc in range(1,11):
    T= int(input())
    dc = [-1,1,0,0] #상하
    dr = [0,0,-1,1] #좌우

    ladder = [0]*100
    for i in range(100):
        ladder[i] = list(map(int,input().split()))
    # print(ladder)

    for row in range(100):
        if ladder[99][row] == 2:
            mem = row
    # print(mem)
    ladder[99][mem]=1
    i = 0
    N = 99
    while N >= 0:

        if 1<=mem<=98:
            N = N-1
            if ladder[N][mem+1]:
                while mem <= 98:

                    mem = mem + 1
                    if ladder[N-1][mem] == 1:
                        break
                # break
            elif ladder[N][mem-1]:
                while mem >= 1:
                    mem = mem - 1
                    if ladder[N-1][mem] == 1:
                        break
        elif mem == 0:
            N = N - 1
            if ladder[N][mem + 1]:
                while mem < 98:

                    mem = mem + 1
                    if ladder[N-1][mem] == 1:
                        break
        elif mem == 99:
            N = N - 1
            if ladder[N][mem - 1]:
                while mem > 0:
                    mem = mem - 1
                    if ladder[N - 1][mem] == 1:
                        break




    print('#{} {}'.format(tc,mem))




