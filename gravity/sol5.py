import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    width = int(input())
    boxes = list(map(int, input().split())) # 칸 당 높이 7 4 2 0 0 6 7 0

    # 빈 박스 만들기
    my_list = [[0] * width for _ in range(width)]

    # 회전한 상태로 박스 채우기
    for i in range(width):
        for j in range(boxes[i]):
            my_list[i][j] += 1
    #print(my_list)

    # 가로 기준으로 세로 줄을 돌며 빈칸 개수 세기
    my_max = 0
    for j in range(width):
        for i in range(width):
            count = 0
            temp = 0
            if my_list[i][j] == 1:
                for idx in range(i+1, width):
                    if my_list[idx][j] == 1:
                        count += 1
                temp = width - i-1 - count
                #print(temp)
                if my_max < temp:
                    my_max = temp
            # 다중 for문 break

    print('#{} {}'.format(tc, my_max))