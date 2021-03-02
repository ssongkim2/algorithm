import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    T = int(input())

    numbers = list(map(int, input().split()))
    total = 0
    for idx in range(2, len(numbers)-2):
        if numbers[idx] > numbers[idx-2] and numbers[idx] > numbers[idx-1] and numbers[idx] > numbers[idx+1] and numbers[idx] > numbers[idx+2]:
            number = [numbers[idx-2],numbers[idx-1],numbers[idx+1],numbers[idx+2]]
            for i in range(len(number)):
                for j in range(len(number)-i-1):
                    if number[j] > number[j+1]:
                        number[j], number[j+1] = number[j+1], number[j]
            result = numbers[idx] - number[3]

            total += result


    print('#{} {}'.format(tc, total))





