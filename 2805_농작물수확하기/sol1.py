import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    F = int(input())
    numbers = [[0] for _ in range(F)]
    for idx in range(F):
        numbers[idx] = input()
    cnt = 0
    i = F//2
    j = F//2 + 1
    for row in range(F//2+1):
        for col in range(i,j):
            cnt += int(numbers[row][col])
        i -= 1
        j += 1
    i += 2
    j -= 2

    for row in range(F//2+1,F):
        for col in range(i,j):
            cnt += int(numbers[row][col])
        i += 1
        j -= 1
    print('#{} {}'.format(tc,cnt))