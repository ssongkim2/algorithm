p = "is"
t = "Thaaaisaisaais a bookis"
result = 0
cnt = 0
def BruteForce(p, t):
    i = 0
    j = 0
    m = len(p)
    n = len(t)
    while j < m and i < n:
        if t[i] != p[j]:          #먼저 비교
            i = i-j               #한칸 옮기기
            j=-1                  #그러기 위해서 j = -1
        i = i+1                   #같다면 i+1
        j = j+1                   #다음 비교를 위해 j+1
    if j == m :                   #j가 m까지 왔다면(패턴문자를 끝까지 다본것이므로 return)
        return i - m
    else : return -1
while result >= 0:
    result = BruteForce(p,t)
    t = t[result+len(p):]
    # print(t)
    # print(result)
    cnt += 1

# print(t)
print(cnt-1)


def bruteforce(p,t):              #p 찾으려는 문자열
    i = 0                         #t 전체 문자열
    j = 0
    m = len(p)
    n = len(t)
    while i<n and j<m:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == m:
        return i - m
    else:
        return -1