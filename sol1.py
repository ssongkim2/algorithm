import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(len(1,T+1)):
    F, N = map(int, input().split())
    word = [list(input()) for _ in range(F)]
    print(word)