import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int,input().split())
    numbers = list(map(int,input().split()))
    tmp = 0
    while True:
        tmp = numbers.pop(0)
        numbers.append(tmp)
    print('#{} {}'.format(tc,numbers[0]))
