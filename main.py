def bruteforce(p,t):
    i = 0
    j = 0
    m = len(p)
    n = len(t)
    while i < n and j < m:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == m:
        return i-m
    else:
        return -1