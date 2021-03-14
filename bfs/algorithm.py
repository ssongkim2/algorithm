def bfs(S,G):
    visited = [False for _ in range(V+1)]
    queue = []
    distance=[0]*[V+1]
    queue.append(S)
    visited[S] = True
    while queue:
        cur = queue.pop(0)
        for i in graph[cur]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                distance[i] = distance[cur]+1