import sys
sys.stdin = open('s_input.txt')
T = int(input())
for tc in range(1, T+1):
    distance, A, B, paris = map(int,input().split())
    # print(paris)
    cnt = 0
    mok = 0
    mok = distance/(A+B)
    print('{} {}'.format(tc, paris*mok))

