import sys
sys.stdin = open('sample_input.txt')

def inorder(N):
    if N < V+1:
        inorder(2*N)
        result.append(N)
        inorder(2*N+1)

#중위순회
T = int(input())
for tc in range(1, 1+T):
    result = []
    ans = 0
    ans2 = 0
    V = int(input())           #노드갯수
    inorder(1)
    for idx in range(len(result)):
        if result[idx] == 1:
            ans = idx+1                         #인덱스는 0부터 시작
        if result[idx] == V//2:                 #인덱스가 도는 순서가 V//2이면
            ans2 = idx+1                        #인덱스는 0부터 시작
    print('#{} {} {}'.format(tc, ans, ans2))
    # print(result)

