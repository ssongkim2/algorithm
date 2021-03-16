import sys
sys.stdin = open('sample_input.txt')

#sol 한달단위 , 세달전과 세달더한것과 한달단위, 지금까지 일년 최솟값과 일년값과의 비교
def solution():
    distance = []
    queue = [0]
    front = -1
    end = 0
    while end < len(month):
        min_money = min(month[end] * cost[0], cost[1]) + queue[end]
        queue.append(min_money)
        end += 1
        if end >= 3:
            front += 1
            queue[end] = min(queue[end], queue[front] + cost[2])


    return min(queue[-1], cost[-1])



T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    month = list(map(int,input().split()))
    print(solution())