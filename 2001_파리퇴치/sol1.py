import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    dc = [0, 1, 0, 1]
    dr = [0, 0, 1, 1]

    list_b = list(map(int, input().split()))
    list_p = [0]*list_b[0]
    for i in range(list_b[0]):
        list_p[i] = list(map(int, input().split()))
    result = []
    for col in range(list_b[0]-list_b[1]+1):
        for row in range(list_b[0]-list_b[1]+1):
            total = 0
            for mode in range(list_b[1]):
                for mode2 in range(list_b[1]):
                    testC = mode + col
                    testR = mode2 + row
                    total += list_p[testC][testR]
            result.append(total)


    for i in range(len(result)):
        for j in range(0, len(result) - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    print('#{} {}'.format(tc,result[-1]))



