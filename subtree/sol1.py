import sys
sys.stdin = open('sample_input.txt')

def preorder(N):
    global cnt
    cnt += 1
    if len(node[N]) == 0:
        return
    for i in node[N]:
        preorder(i)
                                  #순회
                                  #어쨌든 한 뎁스 내려가면 +1



T = int(input())
for tc in range(1, T+1):
    cnt = 0
    E, N = map(int, input().split())
    node = [[]for _ in range(E+2)]         #E+1 까지 존재 따라서 인덱스 고려해서 E+2까지
    node_list = list(map(int, input().split()))
    for idx in range(0, len(node_list)-1, 2):
        node[node_list[idx]].append(node_list[idx+1])
    # print(node)
    preorder(N)
    print('#{} {}'.format(tc, cnt))

    #left right로 받았다면 tree형태로 받았겠지만 index의 node로 받아서... 인덱스 에러가 떠서 dfs같이  풀었습니다...
    #tree 느낌으로 풀려면 left, right로 받아야 할듯 합니다...