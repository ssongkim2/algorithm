import sys
sys.stdin = open('input.txt')

dr1 = [1,0]
dc1 = [0,1]   #하우

def solution(matrix):
    box = 0
    result = []
    queue = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] !=0:
                distance_r = 0
                distance_c= 0
                box += 1
                nr1 = row + dr1[0]
                nc1 = col + dc1[1]
                while 0 <= nr1 < N and matrix[nr1][col] != 0:     #아래로 계속보내기
                    distance_r += 1
                    nr1 = nr1 + dr1[0]
                while 0 <= nc1 < N and matrix[row][nc1] != 0:     #오른쪽으로 계속보내기
                    distance_c += 1
                    nc1 = nc1 + dc1[1]
                if distance_c > 0 or distance_r > 0:
                    for nr in range(distance_r+1):
                        for nc in range(distance_c+1):
                            matrix[row + nr][col + nc] = 0
                result.append([distance_r+1,distance_c+1])
    return result

# def counting_sort(idx):
#     cnt = [0] * 10001
#     sort_ans = [0] * len(result1)
#
#     for i in range(len(result1)):
#         cnt[result1[i][idx]] += 1
#
#     for i in range(1, len(cnt)):
#         cnt[i] += cnt[i-1]
#     for i in range(len(result1)-1,-1,-1):
#         sort_ans[cnt[result1[i][idx]-1] = result1[i]]
#         cnt[result[i][idx]]-=1

def
#이거 버블정렬로 짜보자!


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    matrix = [0]*N
    for idx in range(N):
        matrix[idx] = list(map(int, input().split()))
    result1 = solution(matrix)
    # cnt = [0] * 10001
    # result2 = [0] * len(result1)
    #
    # for i in range(len(result1)):
    #
    # result1.sort(key =lambda x:(x[0]*x[1],x[0]))
    # print('#{} {}'.format(tc, len(result1)), end=" ")
    # for i in range(len(result1)):
    #     print('{} {}'.format(result1[i][0],result1[i][1]), end=" ")
    # print()

    # for i in range(len(result1)):
    #     for j in range(len(result1)-1):
    #         if result[j]
    # print(solution(matrix))