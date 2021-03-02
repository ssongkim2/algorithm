import sys
sys.stdin = open('sample_input.txt')
T = int(input())
# class stack:
#     def __init__(self):
#         self.data = []
#     def push(self,data):
#         self.data.append(data)
#     def pop(self):
#         if self.is_empty == False:
#
#             return self.data.pop()
#         else :
#             return None
#     def is_empty(self):
#         if len(self.data) == 0:
#             return True
#         else: return False
# def is_empty

def solution(numbers):
    stack1 = []
    result = 0
    for idx in range(len(numbers)):
        if numbers[idx].isdigit():
            stack1.append(int(numbers[idx]))
        elif len(stack1)>1:
            if numbers[idx] == '+':
                stack1.append(stack1.pop() + stack1.pop())

            elif numbers[idx] == '*':
                stack1.append(stack1.pop() * stack1.pop())

            elif numbers[idx] == '/':
                stack1.append(stack1.pop() / stack1.pop())
            elif numbers[idx] == '-':
                stack1.append(stack1.pop() - stack1.pop())


        else:
            if numbers[idx] == '.':
                return stack1.pop()
            else:
                return 'error'




for tc in range(1,T+1):
    numbers = list(input().split())
    print('#{} {}'.format(tc,solution(numbers)))
