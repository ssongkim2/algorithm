import sys
sys.stdin = open('sample_input.txt')
#slice로 찾아보기
T = int(input())
for tc in range(1, T+1):
    word = list(map(str,input().split()))
    if word[1]