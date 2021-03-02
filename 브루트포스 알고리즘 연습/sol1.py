def bruteforce(p,t):
    #p 찾으려는 문자열
    #t 전체 문자열
    m = len(p)
    n = len(t)
    i = 0
    j = 0
    while j < m and i < n:
        if t[i] != p[j]:
            i = i - j
            j =-1
        i = i+1
        j = j+1
        if j == m:
            return i-m
        else:
            return -1

print(bruteforce('is','thisisisisisisisisis'))

