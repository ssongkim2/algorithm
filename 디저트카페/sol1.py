import sys
sys.stdin = open('sample_input.txt')


dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
#처음시작은 네방향이어야 하나 그다음부터는 그방향 혹은 90도 회전만 가능
#같은 숫자
#이문제 푸는법 종료조건들 다주고
#direction도 넘겨줌 재귀 호출 할때 그리고 방향이 같다면 계속 보내고 아니라면 direction에 +1해서 봄 그리고 direction이
#N이 된다면 returnㄴㄷㄷ
def dfs(graph, desert, x, y, direct, endx, endy, ans):
    xx = x + dx[direct]
    yy = y + dy[direct]

    if xx >= len(graph) or xx < 0 or yy >= len(graph) or yy < 0:
        return
    if xx == endx and yy == endy:
        ans.append(desert[graph[x][y]]) #마지막에 바로전꺼를 ans에 넣음
        return
    if desert[graph[xx][yy]] != 0:    #이걸로써 desert에 +1해가면서 visited와 갯수를 판별
        return

    desert[graph[xx][yy]] = desert[graph[x][y]] + 1     #마지막으로 앞에 조건들이 아니면
    dfs(graph, desert, xx, yy, direct, endx, endy, ans) #같은거로도 쭉 보내봄
    if direct + 1 < len(dx):                            #이코드로 계속 두갈래로 보내는거
        dfs(graph, desert, xx, yy, direct + 1, endx, endy, ans)
    desert[graph[xx][yy]] = 0                                #이코드로 콜스택에서 리턴된 desert 좌표를 다 0으로 만들어버림 콜스태겡 xx,yy가 들어감 따라서
                                                             #그 xx,yy가 리턴되면서 여기에 있는 desert에 결려서 다 0으로 만들고 돌아감


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
    desert = [0] * 101
    ans = [-1]

    for i in range(N):
        for j in range(1, N - 1):
            desert[cafe[i][j]] = 1
            dfs(cafe, desert, i, j, 0, i, j, ans)
            desert[cafe[i][j]] = 0

    print("#%d" % (t), max(ans))
