import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    F = int(input())
    numbers = list(map(int, input().split()))
    number = numbers[::]
    for i in range(len(number)):
        for j in range(len(number)-i-1):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]

    # print(number[-1])
    result = [0]*number[-1]
    result2 = [1]*numbers[-1]
    result3 = []
    result[0] = list(map)
    for row in range(F):
        for col in range(numbers[row]):


    print(result)

    # for idx in range(F):
