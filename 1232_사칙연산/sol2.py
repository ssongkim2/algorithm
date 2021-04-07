import sys
sys.stdin = open('input.txt')

def cal(a, b, c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    else:
        return a//b

#연산자가 있는 리스트는 모두 스택에 넣고 아래에서부터(스택에 뒤에서 부터) 계산해서 연산자가있는 노드를 숫자로 채워간다는 concept

for tc in range(1,11):
    V = int(input())
    numbers = [0] * (V+1)
    stack = []
    for _ in range(V):
        num = list(input().split())
        if len(num) == 4:                #연산자포함된 노드
            stack += [num]
    # print(stack)
        else:
            numbers[int(num[0])] = int(num[1])
    # print(numbers)
    for i in range(len(stack)-1,-1,-1):
        numbers[int(stack[i][0])] = cal(numbers[(int(stack[i][2]))], numbers[int(stack[i][3])], stack[i][1])
        #자식노드에서 연산결과 부모노드에 저장
    print('#{} {}'.format(tc, numbers[1]))