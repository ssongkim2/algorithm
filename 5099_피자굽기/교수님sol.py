import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())   #N:화덕의 크기, M:피자의 개수
    pizza = list(map(int,input().split()))
    firepot = []         #화덕생성
    for i in range(N):
        firepot.append((i+1,pizza[i]))          #튜플로 넣음

    #피자를 N번부터 넣어야함.
    next_pizza = N
    last_pizza = -1

    while firepot:
        num, cheese = firepot.pop(0)

        cheese //= 2
        last_pizza = num
        if cheese:
            firepot.append((num, cheese))           #튜플
        else:
            if next_pizza < M:
                firepot.append((next_pizza+1, pizza[next_pizza]))
                next_pizza += 1                                  #치즈가 없다면  다음피자를 넣어라