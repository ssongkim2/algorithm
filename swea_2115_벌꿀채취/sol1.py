import sys
from itertools import combinations
sys.stdin = open('sample_input.txt')

def solution(N, M):
    num1 = []
    num2 = []
    sum1 = 0
    sum2 = 0
    max = 0
    for row in range(N):
        for col in range(N-M+1):
            num1 = numbers[row][col:col+M]            #여기서 잘라서 들어가는게 어차피 리스트
            if (col + M) > N:
                continue
            else:
                for row2 in range(row, N):
                    if row2 == row:
                        A = col + 1                   #같은줄 일때
                    else:
                        A = 0                         #다른줄일때
                        for col2 in range(A, N-M+1):
                            num2 = numbers[row2][col2:col2+M]
                            max1 = 0
                            max2 = 0
                            for K in range(0, M+1):
                                result1 = list(combinations(num1, K))
                                result2 = list(combinations(num2, K))
                                                                                    #부분집합 다 구하기

                                for i1 in result1:                                   #result1 안에 값들
                                    sum1 = sum(i1)
                                    total1 = 0
                                    if sum1 > C:
                                        continue
                                    else:
                                        for d1 in i1:
                                            total1 += d1 ** 2
                                            if total1 > max1:
                                                max1 = total1
                                            else:
                                                continue
                                for i2 in result2:
                                    sum2 = sum(i2)
                                    total2 = 0
                                    if sum2 > C:
                                        continue
                                    else:
                                        for d2 in i2:
                                            total2 += d2 ** 2
                                            if total2 > max2:
                                                max2 = total2
                                            else:
                                                continue
                            if max1 + max2 > max:
                                max = max1 + max2
    return max


                                                           #부분집합의 인자의 합이 C보다 크면
#디버그 한번만 해보면 될듯?
#이제 구현할 것 부분집합으로 받아서(조합으로 1에서 M까지) 늘려가며 비교 하고 부분집합 안에 값이 K이상이면 skip
#이하이면 최대값이랑 비교하면서 keep going
#튜플을 풀어내서 제곱으로 ㄱㄱ

T = int(input())
for tc in range(1, 1+T):
    N, M, C = map(int, input().split())
    numbers = [0]*N
    num1 = []
    for idx in range(N):
        numbers[idx] = list(map(int, input().split()))
    print('#{} {}'.format(tc,solution(N, M)))

