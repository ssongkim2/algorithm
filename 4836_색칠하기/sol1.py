import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    F = int(input())
    list_t = [0]*F
    for i in range(F):
        list_t[i] = list(map(int, input().split()))
    list_r = []
    print(list_t)
    # for col in range(len(list_t)):
    #     for row in range(len(list_t[0])):

