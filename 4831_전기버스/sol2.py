import sys
sys.stdin = open('sample_input.txt')

T = int(input())
F = []
for tc in range(T):
    F = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    result = 0
    for idx in range(len(numbers)-1):
        if numbers[idx+1]-numbers[idx] > F[0]:
            result = 0
            break
        else:
            if (F[1]/F[0]) <= (F[0] + 1/F[0]):
                result = int(F[1]/F[0])

    print('#{} {}'.format(tc+1, result))