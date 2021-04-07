import sys
sys.stdin = open('input.txt')


T=int(input())
dc = [-1.1,0,0]
dr = [0,0,-1,1]

for tc in range(1,T+1):
    F=int(input())
    result = [[0for _ in range(F)]for _ in range(F)]
    while True:
        


