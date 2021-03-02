import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    list_b = list(map(int, input().split()))

    l = list_b[1]
    c = list_b[2]
    start = 1
    end = list_b[0]
    cnt = 0
    print(end)
    print(list_b)
    while start == end:
        mid = (start+end)//2
        cnt += 1
        if mid == l:
            break
        elif mid > l:
            end = mid-1
        elif mid < l:
            start = mid+1
    start2 = 0
    end2 = list_b[0]
    cnt2 = 0
    while start2 == end2:
        mid = (start2+end2)//2
        cnt2 += 1
        if mid == c:
            break
        elif mid > c:
            end2 = mid
        elif mid < c:
            start2 = mid

    if cnt > cnt2:
        result = 'A'

    elif cnt < cnt2:
        result = 'B'

    elif cnt == cnt2:
        result = 0

    print(result)