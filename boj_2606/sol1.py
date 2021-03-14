import sys
sys.stdin = open('input.txt')

def solution(S):
    stack = [S]
    visited = [False for _ in range(N+1)]
    cnt=0
    while stack:
        current = stack.pop()
        if visited[current] == False:
            visited[current] = True
            cnt += 1
        stack+=graph[current]
    return cnt-1

N = int(input())
M = int(input())
cnt = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    S, G = map(int,input().split())
    graph[S].append(G)
print(solution(1))
