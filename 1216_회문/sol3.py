import sys
sys.stdin = open("input.txt")

def my_find(M):
    #전체 크기가 N이다
    for i in range(N):
        #부분문자열의 시작점
        for j in range(N-M+1):
            #스왑을 이용한 회문검사
            for k in range(M//2):
                if words[i][j+k] != words[i][j+M-1-k]:
                    break
                elif k ==M//2-1:
                    return M
                    #회문이다
            for k in range(M//2):
                if words[j+k][i] != words[j+M-1-k][i]:
                    break
                elif k == M//2 -1:
                    return M


    return 0

for tc in range(1,11):
    tc_num = int(input())

    N = 100

    words = [input() for i in range(N)]
    #가장 길이가 긴 회문검사를 한다.
    for i in range(N, 0, -1):
        ans = my_find(i)

        if ans!= 0:
            break

    print('{} {}'.format(tc_num, ans))
