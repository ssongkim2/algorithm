import sys
sys.stdin = open('input.txt')


T=int(input())
dc = [-1.1,0,0]
dr = [0,0,-1,1]

for tc in range(1,T+1):
    F=int(input())
    result = [][]
    for col in range(F):
        for row in range(F):
            for mode in range(4):
                testC = col + dc[mode]
                testR = row + dr[mode]

