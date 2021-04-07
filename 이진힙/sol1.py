import sys
sys.stdin = open('sample_input.txt')

def preorder(N):
    if N < V+1:
        result[N] = numbers[N-1]
        if N >= 2:
            if result[(N//2)] > result[N]:
                result[(N//2)], result[N] = result[N], result[(N//2)]         #정렬

        preorder(2*N)
        preorder(2*N+1)


#중위순회
T = int(input())
for tc in range(1, 1+T):
    V = int(input())
    ans = 0
    result = [0] * (V + 1)
    numbers = list(map(int, input().split()))
    preorder(1)
    # result.pop(0)
    # print(result)
    idx = len(result)-1                  #머자먹원소
    if idx < 1:
        continue
    while idx != 1:
        idx = idx // 2
        ans += result[idx]
    print('#{} {}'.format(tc, ans))


