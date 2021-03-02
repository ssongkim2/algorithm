import sys
sys.stdin = open('sample_input.txt')

def solution(omok):
    for col in range(F):
        for row in range(F):
            #가로판정
            if omok[col][row] and omok[col][row+1] and omok[col][row+2] and omok[col][row+3] and omok[col][row+4]:
                return 'YES'
            #대각선 판정(왼>>오)
            if omok[col][row] and omok[col+1][row+1] and omok[col+2][row+2] and omok[col+3][row+3] and omok[col+4][row+4]:
                return 'YES'
            if omok[col][row+4] and omok[col+1][row+3] and omok[col+2][row+2] and omok[col+3][row+1] and omok[col+4][row]:
                return 'YES'
            if omok[col][row] and omok[col+1][row] and omok[col+2][row] and omok[col+3][row] and omok[col+4][row]:
                return 'YES'

    return 'NO'
#이거 함수로 짜길 잘했다... for문 두개 나와야 하니까...

def mixit(dol):
    pan = [[0]*(F+4) for _ in range(F)]
    pan.append([0] * (F + 4))
    pan.append([0] * (F + 4))
    pan.append([0] * (F + 4))
    pan.append([0] * (F + 4))
    for col in range(F):
        for row in range(F):
            if dol[col][row] == '.':
                pan[col][row] = 0
            if dol[col][row] == 'o':
                pan[col][row] = 1
    return pan


T = int(input())
for tc in range(1,T+1):
    F = int(input())
    dol = []
    for i in range(F):
        dol.append(input())
    result = mixit(dol)
    print('#{} {}'.format(tc,solution(result)))
