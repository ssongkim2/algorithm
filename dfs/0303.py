class queue:
    def __init__(self):
        self.data = []
        self.front = -1
        self.rear = -1
    def enqueue(self,data):
        self.rear += 1
        self.data.append(data)
    def dequeue(self):
        self.front += 1
        return self.data.pop(0)
    def is_empty(self):
        if len(self.data) <= 0:
            return True
        return False
    def is_full(self):
        if self.front == self.rear:
            return True
        else:
            return False


def bfs(graph,S):
    visited = [False for _ in range()]
    to_visit = [S]
    while to_visit:
        current = to_visit.pop(0)
        if visited[current] == False:
            visited[current] = True
            to_visit += graph[current]


