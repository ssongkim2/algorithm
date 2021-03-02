import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    list_r = [0]*5001
    result = []
    N = int(input())
    for n in range(N):
        bus = list(map(int, input().split()))
        for idx in range(bus[0], bus[1] + 1):
            list_r[idx] += 1
    P = int(input())
    list_P = []
    for i in range(P):
        stop = int(input())
        list_P += [stop]
    result = []
    for i in range(len(list_P)):
        result += [list_r[list_P[i]]]

    print('#{} {}'.format(tc, ' '.join(map(str, result))))


