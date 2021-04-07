import sys
sys.stdin = open('input.txt')

def postorder(N):
    if N < V+1:
        postorder(2*N)
        postorder(2*N+1)
        if numbers[N].isdigit():
            stack.append(int(numbers[N]))
        else:
            if numbers[N] == '-':
                cur1 = stack.pop()
                cur2 = stack.pop()
                stack.append(cur2-cur1)
            elif numbers[N] == '*':
                cur1 = stack.pop()
                cur2 = stack.pop()
                stack.append(cur2*cur1)
            elif numbers[N] == '/':
                cur1 = stack.pop()
                cur2 = stack.pop()
                stack.append(cur2//cur1)
            elif numbers[N] == '+':
                cur1 = stack.pop()
                cur2 = stack.pop()
                stack.append(cur2+cur1)

#완전이진트리가 아니라서 버려야함
for tc in range(1, 11):
    stack = []
    V = int(input())
    numbers = [0]*(V+1)
    for _ in range(V):
        info = list(input().split())
        numbers[int(info[0])] = info[1]
    postorder(1)
    print(stack)

