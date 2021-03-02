import sys
sys.stdin = open('input.txt')

def solution(arr1,S,G):
    visited=[False for _ in range(100)]
    to_visit = [S]
    while to_visit:
        current = to_visit.pop()
        # if now == 99:
        #     return 1      이러면 완전탐색은 아니지만 최적화는 된 코드
        if not visited[current]:                             #visited[current]가 false일 경우
            visited[current] = True
            to_visit += arr1[current]                        #여기 리스트로 들어가면 안됨! 그래서 += 여기라인 공부하기!!!
    return int(visited[G])

for tc in range(1, 11):
    T, N = map(int,input().split())
    numbers = list(map(int,input().split()))
    S = 0
    G = 99
    arr1 = [[] for _ in range(100)]
    for idx in range(len(numbers)//2):                  #이거 2로안나누고 스탭으로 해도됨
        arr1[numbers[2*idx]].append(numbers[2*idx+1])
    print('#{} {}'.format(tc,solution(arr1,S,G)))
