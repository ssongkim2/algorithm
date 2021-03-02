import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    T = int(input())
    sik = input()
    stack = []
    number = []
    # print(sik)
    for idx in range(T):
        if not sik[idx] == '+' or '*':
            stack.append(sik[idx])
        else:
            number.append(sik[idx])
    print(stack)
    # print(number)