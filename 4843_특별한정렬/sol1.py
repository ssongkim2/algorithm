import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    F = int(input())
    numbers = list(map(int,input().split()))
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = []
    for idx in range(len(numbers)//2):
        result.append(numbers[idx*(-1)-1])
        result.append(numbers[idx])

    result2 = []
    for idx in range(10):
        result2.append(result[idx])

    print('#{} {}'.format(tc, ' '.join(map(str, result2))))