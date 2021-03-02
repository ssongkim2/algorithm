import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    numbers = []
    cnt = [0]*10
    for _ in range(9):
        numbers.append(list(map(int, input().split())))
    # print(numbers)
    i = 0
    j = 0
    result = 0
    total = 0
    while i<7 and j<7:
        #사각형
        cnt = [0] * 10
        for row in range(i,i+3):
            for col in range(j,j+3):
                cnt[numbers[row][col]] = 1
        for idx in range(10):
            total += cnt[idx]
        #가로돌리기
        for row in range(i,i+3):
            cnt = [0] * 10
            for col in range(9):
                cnt[numbers[row][col]] = 1
            for idx in range(10):
                total += cnt[idx]

        #세로돌리기
        for col in range(i,i+3):
            cnt = [0] * 10
            for row in range(9):
                cnt[numbers[row][col]] = 1
            for idx in range(10):
                total += cnt[idx]
        i += 3
        j += 3
    # print(total)
    if total == 189:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(tc,result))

