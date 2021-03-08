import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    queue = [0]*N
    tip = -1
    idx2 = N
    result = []
    for idx in range(N):
        queue.append(pizzas[idx])
    while len(result) == M:
        tip += 1
        if tip >= len(queue):
            tip = tip % len(queue)
        if queue[tip] < 1:
            if idx2 >= M-1:
                result.append(queue.pop(tip))
                tip -= 1
            else:
                result.append(queue[tip])
                queue[tip] = pizzas[idx2]
                idx2 += 1
        queue[tip] = queue[tip]//2
    # queue.pop(1)
    # queue[1] = pizzas[3]
    print(result)
    # print(result)