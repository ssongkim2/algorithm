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
                result.append([distance_r+1,distance_c+1,(distance_r + 1)*(distance_c + 1)])
    return result

def bubble_sort(matrix,idx1,idx2):
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):

            if matrix[j][idx1] > matrix[j+1][idx1]:
                matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            if matrix[j][idx1] == matrix[j+1][idx1]:
                if matrix[j][idx2] > matrix[j+1][idx2]:
                    matrix[j],matrix[j+1] = matrix[j+1], matrix[j]

    return matrix

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    matrix = [0]*N
    for idx in range(N):
        matrix[idx] = list(map(int, input().split()))
    result1 = solution(matrix)
    # print(result1)
    bubble_sort(result1,2,0)
    # bubble_sort(result1)
    print('#{} {}'.format(tc,len(result1)), end=" ")
    for row in range(len(result1)):
        print('{}'.format(' '.join(map(str,result1[row][0:2]))), end=" ")
    print()


