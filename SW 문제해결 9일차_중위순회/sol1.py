import sys
sys.stdin = open('input.txt')

def inorder(num):
    if num < V+1:
        inorder(2*num)
        print(tree_list[num], end='')
        inorder(2*num + 1)
    else:
        return


for tc in range(1, 11):
    result = []
    V = int(input())
    tree_list = [0]*(V+1)          #트리를 담을 리스트
    for _ in range(V):
        i = list(input().split())
        tree_list[int(i[0])] = i[1]         #노드번호에 알파벳 저장
    # print(tree_list)
    print('#{} '.format(tc), end='')
    inorder(1)
    print()                               #엔터

