import sys
sys.stdin = open('sample_input.txt')

T = int(input())

class stack:
    def __init__(self):
        self.data = [A]
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
    def wordlen(self):
        return len(self.data) - 1



for tc in range(1,T+1):
    words = input()
    s = stack()
    cmp = []
    result = ''
    for idx in range(len(words)):
        s.push(words[idx])


    result = s.wordlen()
    print(result)



    # idx = 0
    # while True:
    #     if words[idx] == words[idx+1]:


