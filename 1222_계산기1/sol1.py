import sys
sys.stdin = open('input.txt')
for tc in range(1,11):
    F = int(input())
    numbers = input()
    stack_num = []
    stack_
    for idx in range(F):
        if numbers[idx] != '+':
            stack.append(int(numbers[idx]))
    total = 0
    for idx in range(len(stack)):
        total += stack[idx]
    print('#{} {}'.format(tc,total))