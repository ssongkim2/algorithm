import sys
sys.stdin = open('input.txt')

class stack:
    def __init__(self):
        self.data = ['A']
    def push(self,data):
        if data != self.data[-1]:
            self.data.append(data)
        else:
            self.data.pop()
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
    def password(self):
        return self.data



for tc in range(1,11):
    T, words = map(str,input().split())
    s = stack()
    cmp = []
    result = ''
    for idx in range(len(words)):
        s.push(words[idx])


    result = s.password()
    result1 = result[1:]
    print('#{} {}'.format(tc,''.join(map(str,result1))))
