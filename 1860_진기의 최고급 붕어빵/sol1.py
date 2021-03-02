import sys
sys.stdin = open('input.txt')

def solution(numbers,N,M,K):
    time = 0
    cnt = 0
    number = numbers[:]
    for i in range(len(number)):
        for j in range(len(number)-1):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1],number[j]
    for idx in range(N):
        if number[idx] < M:
            cnt+=1
            return 'Impossible'
        elif (number[idx]//M)*K < idx:
            return 'Impossible'
    return 'Possible'
T =  int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    numbers = list(map(int,input().split()))
    print('#{} {}'.format(tc,solution(numbers,N,M,K)))