import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, 1+T):
    N, M, L = map(int, input().split())
    node = [0] * (N+1)
    for _ in range(M):
        S, G = map(int,input().split())
        node[S] = G
    for idx in range(N//2, 0, -1):
        if idx*2 == N:
            node[idx] = node[idx*2]                  #노드를 그냥올라가야할때
        if node[idx] == 0:
            node[idx] = node[idx*2] + node[idx*2+1]  #노드의 합

    print('#{} {}'.format(tc,node[L]))