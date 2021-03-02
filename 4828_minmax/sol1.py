import sys
sys.stdin = open('sample_input.txt')

T = int(input())
result = 0
for tc in range(1, T+1):
    F = int(input())
    number = list(map(int, input().split()))
    for i in range(F):
        for j in range(F-1-i):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
    result = number[F-1] - number[0]
    print('#{} {}'.format(tc,result))