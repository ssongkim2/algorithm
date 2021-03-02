import sys
sys.stdin = open('input.txt')


for tc in range(1,11):
    T = int(input())
    list_d = [list(map(int, input().split())) for _ in range(100)]
    result = []
    # print(list_d)
    for col in range(100):
        total1 = 0
        for row in range(100):
            total1 += list_d[row][col]
        result.append(total1)
    for row in range(100):
        total2 = 0
        for col in range(100):
            total2 += list_d[row][col]
        result.append(total2)
    for col in range(100):
        total3 = 0
        for row in range(100):
            if col == row:
                total3 += list_d[row][col]
            else:
                continue

        result.append(total3)
    for col in range(100):
        total4 = 0
        for row in range(100):
            if col == row:
                total4 += list_d[99-row][col]

    for i in range(len(result)):
        for j in range(0, len(result)-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]

    print('#{} {}'.format(tc, result[-1]))
