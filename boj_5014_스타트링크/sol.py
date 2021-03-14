import sys
sys.stdin = open('input.txt')

def solution(S,G):
    queue = [0]*1000000
    front = -1
    rear = 0
    cnt = 0
    visited = [False for _ in range(1+F+U)]
    queue[rear].append(S)
    while rear != front:
        front += 1
        cur = queue[front]
        if cur != G and visited == False:
            if cur < G:
                cur = cur + U
                rear += 1
                queue[rear] = cur
            else:
                cur = cur - D
                rear += 1
                queue[rear] = cur
        elif cur == G:
            return cnt
    return 0
s

T=int(input())
for tc in range(1,1+T):
    F, S, G, U, D = map(int,input().split())
