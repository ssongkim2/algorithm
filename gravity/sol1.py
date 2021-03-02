import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    F = int(input())
    numbers = list(map(int, input().split()))
    cnt_max = 0
    idx_max = 0
    zero_chk = 0
    zero_max = 0
    idx_chk = 0
    result = 0
    for idx in range(F):
        cnt = 0
        for i in range(F-idx):
            if numbers[idx] > numbers[idx+i]:
                cnt += 1
            else:
                if cnt >= cnt_max:
                    cnt_max = cnt

    if cnt_max == 0:
        for idx in range(F):
            if 

    else:


        for idx in range(F):
            if numbers[idx] == 0:
                idx_chk = idx
        zero_chk = F - idx_chk
        result = cnt_max + zero_chk
    print('#{} {}'.format(tc, result))




