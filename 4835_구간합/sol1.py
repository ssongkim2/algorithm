import sys
sys.stdin = open('sample_input.txt')\

T = int(input())
F = []

for tc in range(1, T+1):
    F = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    # print(numbers)
    ans = 0
    result = []
    for idx in range(0, F[0]-F[1]+1):
        total = 0
        for i in range(0, F[1]):
            total += numbers[idx+i]
        result.append(total)
        for i in range(len(result)):
            for j in range(len(result)-1-i):
                if result[j] > result[j+1]:
                    result[j], result[j+1] = result[j+1], result[j]

    print('#{} {}'.format(tc, result[-1]-result[0]))

