import sys
sys.stdin = open('sample_input.txt')

T = int(input())
F = []
for tc in range(T):
    F = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    result = [0] * (F[1])

    for idx in range(len(result)):
        for i in range(len(numbers)):
            if idx == numbers[i]:
                result[idx] = 1
    idx = 0
    count = 0
    while ( idx + F[0] < F[1]):
        for j in range(F[0],-1,-1):
            if j == 0:
                count = 0
                idx += F[1]

            elif result[idx + j] == 1:
                count += 1
                idx += j
                break


    print('#{} {}'.format(tc+1,count))


