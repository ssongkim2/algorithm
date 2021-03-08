def dfs(graph,start):
    queue = []
    queue.append(start)
    while queue:
        current = queue.pop()
        for i in graph[current]:
            if visited[i]!=True:
                queue.append(i)

def dfs_recursive(idx):            #다내려가서 visited를 True로 바꾼다는 생각하기!
    visited[idx] == True
    for i in graph[idx]:
        if visited[i] != True
            dfs_recursive(i)