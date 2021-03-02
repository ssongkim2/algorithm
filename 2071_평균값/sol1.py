import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    total = 0
    for idx in range(len(numbers)):
        total += numbers[idx]
    avg = round(total/len(numbers))
    print('#{} {}'.format(tc,avg))

#입력 숫자를 리스트로 바꾼다

#리스트의 총합을 구한다

#총 합을 리스트 원소 개수로 나눈다.
