import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    word = list(map(str,input().split()))
    cnt = 0
    p = word[1] #찾는 패턴
    t = word[0] #문자열 전체

    result = 0
    def bruteForce(p, t): #처음 같은 문자열이 나오는것을 찾음
        i=0
        j=0
        m = len(p)  #찾는 패턴길이
        n = len(t)  #문자열 전체길이
        while j < m and i < n:
            if t[i] != p[j]:
                i = i-j
                j = -1
            i = i+1
            j = j+1
        if j == m:
            return i - m
        else:
            return -1

    while result >= 0:
        result = bruteForce(p, t)
        t = t[result+len(p):]
        # m = len(word[1])
        # n = len(word[0])
        cnt += 1

    result = cnt-1
    result1 = len(word[0]) - (len(p)*result) + result
    print('#{} {}'.format(tc,result1))
    # print(result)




    # print(result)
    # print(word[0],word[1])
    #
    # if word[1] in word[0]:
    #     cnt += 1
    # print(cnt)