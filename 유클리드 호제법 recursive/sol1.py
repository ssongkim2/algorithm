def solution(A,B):
    if A % B == 0:             # 종료조건
        return B
    else:
        return solution(B, A % B)


print(solution(192,162))