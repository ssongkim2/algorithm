import sys
sys.stdin = open('sample_input.txt')

def solution(V, E, graph, S, G):
    #vertex No == visited idx == graph idx
    visited = [False for _ in range(V+1)]
    to_visits = [S]
    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] =True
            to_visits += graph[current]
    return visited[G]

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())  # Vertex, Edge의 갯수
    graph = [[] for _ in range(V+1)] #인덱스 맞추려고 하나를 추가
    for _ in range(E):
        start, end = map(int,input().split())
        graph[start].append(end)
        # graph[end].append(start)  무향 그래프일시 이렇게 씀
    S, G = map(int,input().split())
    print('{} {}'.format(tc,solution(V,E,graph,S,G)))