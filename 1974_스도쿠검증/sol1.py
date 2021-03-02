import sys
sys.stdin = open('input.txt')
T = int(input())
def solution(numbers):
    #사각형 검사
    total1 = 0
    total2 = 0
    total3 = 0
    cmp1 = []
    cmp2 = []
    cmp3 = []
    result = []
    for i in range(6):
        for j in range(6):
            cnt = [0] * 10
            for row in range(i, i + 3):
                for col in range(j, j+3):
                    cnt[numbers[row][col]] = 1
                for idx in range(9):
                    total1 += cnt[idx]
                    if total1 == 9:
                        cmp1.append(1)
                    else :cmp1.append(0)
            for row in range(9):
                cnt = [0] * 10
                for col in range(9):
                    cnt[numbers[row][col]] = 1
                    for idx in range(9):
                        total2 += cnt[idx]
                        if total2 == 9:
                            cmp2.append(1)
                        else: cmp2.append(0)
            for col in range(9):
                cnt = [0] * 10
                for row in range(9):
                    cnt[numbers[row][col]] = 1
                    for idx in range(9):
                        total3 += cnt[idx]
                        if total3 == 9:
                            cmp3.append(1)
                        else: cmp3.append(0)
    for idx in range(len(cmp1)):
        if cmp1[idx] == 1 and cmp2[idx] == 1 and cmp3[idx] == 1:
            result.append(1)
        else:
            result.append(0)
    return result


for tc in range(1,T+1):
    numbers = []
    for _ in range(9):
        numbers.append(list(map(int,input().split())))
    print(solution(numbers))