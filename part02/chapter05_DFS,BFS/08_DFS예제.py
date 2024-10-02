def DFS(graph, node, visited):
    visited[node] = True
    print(node, end=" ")
    for i in graph[node]:
        if not visited[i]:
            DFS(graph, i, visited)

graph = [
    [], 
    [2, 3, 8], 
    [1, 7], 
    [1, 4, 5], 
    [3, 5], 
    [3, 4], 
    [7], 
    [2, 6, 8], 
    [1, 7]
    ]

visited = [False] * 9
DFS(graph, 1, visited)