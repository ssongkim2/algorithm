import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1,T+1):
    F = int(input())
    numbers = list(map(int,input().split()))
    max_cnt = 0
    for i in range(F):
        cnt = 0
        for j in range(F-i-1):
            if numbers[i] > numbers[i+j+1]:
                cnt +=1

        if max_cnt < cnt:
            max_cnt = cnt

    print('#{} {}'.format(tc,max_cnt))

