'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

'''

################ 2024.10.04 ###############
INF = int(1e9)

n = int(input())
v = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)] # 그래프이면서 최단거리 저장?
for _ in range(v):
    startNode, endNode, dist = map(int, input().split())
    graph[startNode][endNode] = dist
for i in range(n+1):
    graph[i][i] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            # 만약 i가 1이면, 2 -> 3이 이득인지 2 -> 1 -> 3이 이득인지 비교해야함
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('INF', end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
###########################################