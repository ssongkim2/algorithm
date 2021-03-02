import sys
sys.stdin = open('sample_input.txt')
result1= 0
result2= []

T = int(input())
for tc in range(1,T+1):
    F = int(input())
    numbers = list(input())
    counter = [0]*10
    idx_list=[]
    result1=[]
    result = 0

    for i in numbers:
        if i in numbers:
            counter[int(i)] += 1

    save = counter[:]

    for i in range(10):
        for j in range(9-i):
            if counter[j] > counter[j+1]:
                counter[j], counter[j+1] = counter[j+1], counter[j]

    result = counter[9]


    for idx in range(10):

        if save[idx] == result:
            result1.append(idx)

    print('#{} {} {}'.format(tc, result1[-1], result))