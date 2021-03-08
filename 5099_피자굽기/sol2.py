import sys
sys.stdin = open('sample_input.txt')
T = int(input())

def solution(pizzas):
    queue = []
    chk = [False for _ in range(M+1)]
    for idx in range(N):
        queue.append(pizzas.pop(0))
        chk[idx+1] = True             #큐에 피자가 들어감
    tmp = 0
    while len(pizzas)>0:
        tmp = queue.pop(0)
        if tmp < 1:
            tmp = pizzas.pop(0)
            queue.append(tmp)
        else:
            queue.append(tmp)
    return queue

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    print(solution(pizzas))
    #pizzas와 큐에 남은피자

