import sys
sys.stdin = open('sample_input.txt')

#sol 한달단위 , 세달전과 세달더한것과 한달단위, 지금까지 일년 최솟값과 일년값과의 비교
def solution(S):
    distance = []
    queue= [S]
    idx = 0
    while len(queue) < len(month):
        idx += 1
        min_money = queue[-1] + min(month[idx] * cost[0], cost[1])
        queue.append(min_money)
        if len(queue) > 3:
            min_money2 = queue[-1] + min(queue[-1], queue[idx-3] + cost[2])
        return min(queue[-1], cost[3])



T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    month = list(map(int,input().split()))
    print(solution(0))
