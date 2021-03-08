import sys
sys.stdin = open('sample_input.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]
#시작정점을 찾는 함수
def search():
    for row in range(N):
        for col in range(N):
            if maze[row][col] == '2':
                return row, col

def BFS(mem_row, mem_col):
    #선형큐를 이용해서 작성을 해부자!
    Q = [0] *1000000
    front = -1
    rear = 0
    #rear가 0 인이유는 rear값을 시작할때 넣어주고 싲가할 거라서
    Q[rear] = (mem_row,mem_col)
    dist = [[-1]*(N) for _ in range(N)]        #미로의 거리를 저장할 리스트
    dist[mem_row][mem_col] = 0
    #선형큐에서의 공백 검사,
    while front != rear:
        front += 1
        cur_row, cur_col = Q[front]
        if maze[cur_row][cur_col] == '3':                    #지금 서있는 위치가 문인지
            return dist[cur_row][cur_col] - 1
        for i in range(4):
            nr = cur_row + dr[i]
            nc = cur_col + dc[i]

            #범위 검사
            if nc<0 or nr >=N or nc<0 or nc>=N: continue              #1이아닌 다음maze로 이동, 여기서 검사하는 알고리즘 짜보자!
            #벽이 아니면서, 거리를 갱신하지 않았다면 좌표를 넣고 갱신, dist가 visited역할도 함
            if maze[nr][nc] != '1' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[cur_row][cur_col] + 1
                rear += 1
                Q[rear] = (nr, nc)
    return 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    mem_row, mem_col = search()