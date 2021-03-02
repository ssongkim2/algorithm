import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_numbers = list(map(int, input().split()))
    M_numbers = list(map(int, input().split()))
    # print(M)
    move = 0
    result = []
    if N > M:
        while move <= N - M:
            total = 0
            for idx in range(move, move+M):
                total += N_numbers[idx] * M_numbers[idx-move]
            result.append(total)
            move += 1

    if N < M:
        while move <= M - N:
            total = 0
            for idx in range(move, move+N):
                total += N_numbers[idx-move] * M_numbers[idx]
            result.append(total)
            move += 1

    #
    # if
    for i in range(len(result)):
        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    print('#{} {}'.format(tc,result[-1]))