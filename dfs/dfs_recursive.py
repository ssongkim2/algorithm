import sys
sys.stdin = open('sample_input.txt')

# def solution(V,E,graph,S,G):
#     to_visit = []
#     visited = [False for _ in range(V+1)]
#     to_visit.append(S)
#     while to_visit:
#         current = to_visit.pop()
#         if visited[current] is not True:
#             visited[current] = True
#             to_visit += graph[current]   #여기서 append로 들어가면 안되는 이유 : 이미 graph요소가 작은 리스트로 되어있음 따라서
#                                          #append로 하배러면 리스트가 들어가버림!!!
#
#
#     return int(visited[G])

# def solution2(V,E,graph,S,G):
#     visited = [False]*(V+1)
#     to_visit = []
#     to_visit.append(S)
#     while to_visit:
#         current = to_visit.pop()
#         if visited[current] is False:
#             visited[current] = True
#         to_visit += graph[current]
#     return int(visited[G])


def solution(idx):
    visited[idx] = True
    for i in graph[idx]:
        if visited[i] != True:
            visited[i] = True

            solution(i)
    return int(visited[G])


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())  # Vertex, Edge의 갯수
    graph = [[] for _ in range(V+1)] #인덱스 맞추려고 하나를 추가
    visited = [False for _ in range(V + 1)]
    for _ in range(E):
        start, end = map(int,input().split())
        graph[start].append(end)
        # graph[end].append(start)  무향 그래프일시 이렇게 씀
    S, G = map(int,input().split())
    # visited = [False for _ in range(V + 1)]
    # print(visited)
    print('#{} {}'.format(tc, solution(S)))