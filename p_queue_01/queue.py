class queue:
    def __init__(self):
        self.data = []
        self.front = -1
        self.rear = -1
    def enqueue(self, value):
        self.data.append(value)
        self.rear += 1

    def dequeue(self):
        self.front += 1
        return self.data[self.front]

    def is_empty(self):
        if self.front == self.rear:
            return True

        return False


    #삭제없이 단순히 맨 앞의 data값을 리턴
    def get_rear(self):
        return self.data[self.rear]


    # 삭제없이 단순히 맨 뒤의 data값을 리턴
    def get_front(self):
        #if self.is_empty():
            # return None
        # else:
        return self.data[self.front+1]

q = queue()
q.enqueue(1) # q.data == 1
print(q.data)
q.enqueue(2)
print(q.data)
print(q.dequeue())    # 1
print(q.dequeue())    # 1
print(q.get_front())  # 1
print(q.get_rear())   # 2
print(q.is_empty())

