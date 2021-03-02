import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, 11):
    F = int(input())
    numbers = list(map(int, input().split()))
    idx =F-1
    i = 0
    cnt = 0
    while idx-i > 0:
        i += 1
        if numbers[idx] - numbers[idx-i] >= 0:
            cnt += numbers[idx] - numbers[idx-i]
        else:
            idx = idx-i
            i = 0
    print('{} {}'.format(tc,cnt))

