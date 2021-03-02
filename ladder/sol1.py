import sys

# from pandas import DataFrame
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    result = [0] * 100
    idx_r = 0
    idx_c = 0
    for i in range(len(result)):
        result[i] = list(map(int, input().split()))
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    test_c = 0
    test_r = 0
    row = 0
    col = 0
    mem = 0
    for row in range(len(result)):
        if result[99][row] == 2:
            mem = row
    # print(mem)
    col2 = 99
    result[col][mem] = 1
    while col2 == 0:
        if result[col - 1][mem] and result[col][mem] == 1:
            result[col][mem] = 0
            col = col - 1
        if result[col][mem + 1] and result[col][mem] == 1:
            result[col][mem] = 0
            mem = mem - 1
        if result[col][mem - 1] and result[col][mem] == 1:
            result[col][mem] = 0
            mem = mem + 1


    print(mem)

    # for row in range(len(result)):
    # while row < len(result):
    #     # for col in range(len(result[row])):
    #     while col < len(result[row]):
    #         while result[col][row] == 1 :
    #
    #             if result[col][row] and result[col+1][row] == 1:
    #
    #                 test_c = col + dc[2]
    #                 col = test_c
    #             elif result[col][row] and result[col][row+1] == 1:
    #                 test_r = row + dr[4]
    #                 row = test_r
    #             # elif result[col][row] and result[col][row-1] == 1:
    #             #     test_r = row + dr[3]
    #             #     row = test_r
    #             if result[test_c][test_r] == 2:
    #                 break
    #
    # print(row)

    # while col<=100:
    #     if result[col][row] and result[col+1][row]  == 1:
    #         col += 1
    #     elif result[col][row] and result[col][row+1] == 1:
    #         row += 1
    #     elif result[col][row] and result[col][row-1] == 1:
    #
    #

    # for row in range(len(result)):
    #     for col in range(len(result[row])):
    #         while

    # if result[col][row] and result[col][row+1] == 1:
    #     idx_r = row + 1
    # elif result[col][row] and result[col+1][row] == 1:
    #     idx_c = col + 1
