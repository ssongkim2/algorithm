import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1,T+1):
    F = int(input())
    numbers = list(map(int,input().split()))
    max_number = numbers[:]
    for i in range(F):
        for j in range(F-1):
            if max_number[j]>max_number[j+1]:
                max_number[j],max_number[j+1] = max_number[j+1],max_number[j]
    # print(max_number)
    list_num = [[0]*max_number[-1] for _ in range(F)]
    # print(list_num)
    for col in range(F):
        for row in range(numbers[col]):
            list_num[col][row] = 1
    max_cnt = 0


    # print(list_num)

    for row in range(max_number[-1]):
        cnt = 0
        list_sum = 0
        for col in range(F):
            list_sum += list_num[col][row]
        if list_sum >= 1:
            for col in range(F):

                if list_num[col][row] == 0:
                    cnt += 1
                if cnt >= max_cnt:
                    max_cnt = cnt
        else : continue

    print('#{} {}'.format(tc, max_cnt))




