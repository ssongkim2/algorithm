import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    result = 0
    T = int(input())
    numbers = list(map(int, input().split()))
    while T > 0:

        for i in range(len(numbers)):
            for j in range(len(numbers)-1-i):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        numbers[0] += 1
        numbers[-1] -= 1
        T -= 1
        # if numbers[-1]-numbers[0] <= 1:
        #     return numbers[-1] - numbers[0]
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    result = numbers[-1] - numbers[0]
    print('#{} {}'.format(tc,result))

