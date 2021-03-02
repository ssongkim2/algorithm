import sys
# from pandas import DataFrame
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())

    puzzle = [[0]+list(map(int,input().split()))+[0] for _ in range(N)]
    puzzle.append([0]*(N+2))
    print(puzzle)
    # ans = 0
    # for i in range(N):
    #      cnt = 0
    #      #벽을 한칸 더 둘렀기 때문에 증가
    #      for j in range(N+1):
    #          if puzzle[i][j]:
    #              cnt += 1
    #          else:
    #              if cnt == K

