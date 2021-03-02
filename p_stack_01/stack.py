import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def solution(words):
    s = stack()
    cmp = ''
    for word in words:
        if word == '(' or word == '{' or word == '[':
            s.push(word)
        elif word == ')':
            cmp = s.pop()
            if cmp != '(':
                return False
        elif word == '}':
            cmp = s.pop()
            if cmp != '{':
                return False
        elif word == ']':
            cmp = s.pop()
            if cmp !='[':
                return False
    if s.is_empty() == False:
        return False
    if s.is_empty() == True:
        return True

class stack:
    def __init__(self):
        self.data = []

    def push(self,data):
        self.data.append(data)

    def pop(self):
        if self.is_empty() != True:
            return self.data.pop()
        else:
            return None

    def is_empty(self):
        if len(self.data) != 0:
            return False
        else:
            return True
for tc in range(1, T+1):
    words = input()
    result = ''
    cmp = ''
    result1 = solution(words)
    if result1 == True:
        result = '1'
    if result1 == False:
        result = '0'

    print('#{} {}'.format(tc,result))