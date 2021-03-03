import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    cmp = []

    room = [[] for _ in range(N)]
    for idx in range(N):
        A, B = map(int, input().split())
        room[idx].append(A)
        room[idx].append(B)
    for row in range(len(room)-1):
        if room[row][1] >= room[row+1][0]:
            cnt += 1
        else:
            continue
    # print(cmp)
    # idx = 0
    # while len(room) != 0:
    #     cmp = room.pop(0)
    #     if cmp[0] < room[idx][0] < cmp[1] or cmp[0] < room[idx][1] < cmp[1]:
    #         continue
    #
    #     else:
    #         room.pop(idx)
    #         idx -= 1
    #         if idx == len(room) :
    #             cnt+=1
    #     idx += 1


    print('#{} {}'.format(tc,cnt+1))