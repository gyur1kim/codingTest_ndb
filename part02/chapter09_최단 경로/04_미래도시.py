'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4

'''
INF = int(1e9)

# 회사 개수 n, 경로 개수 m
n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    startNode, endNode = map(int, input().split())
    graph[startNode][endNode] = 1
    graph[endNode][startNode] = 1

# k회사에서 소개팅 후 x회사에 방문판매
x, k = map(int, input().split())

for i in range(n+1):
    graph[i][i] = 0

for a in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][a] + graph[a][j])

if graph[1][x] == INF or graph[x][k] == INF:
    print(-1)
else: 
    print(graph[1][k] + graph[k][x])
