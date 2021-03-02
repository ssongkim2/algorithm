import sys
sys.stdin = open('input.txt')

def square(N,M):
    if M == 1:
        return N
    else:
        return N*square(N,M-1)

for tc in range(1,11):
    T = int(input())
    N, M= map(int,input().split())
    print(square(N,M))
