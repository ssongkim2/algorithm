import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    bit = list(map(int,input()))
    cmp = [0]*len(bit)
    mem = 0
    cnt = 0
    if bit[0] == 1:
        cnt = 1
    else :
        cnt = 0
    mem = bit[0]
    for idx in range(1,len(bit)):

        if bit[idx] != mem:
            cnt += 1
            mem = bit[idx]
        else:
            continue
    print('#{} {}'.format(tc,cnt))








