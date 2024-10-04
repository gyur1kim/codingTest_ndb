'''
3 2 1
1 2 4
1 3 2

'''
INF = int(1e9)

# 도시 개수 n, 통로 개수 m, 메시지를 보내고자 하는 도시 c
n, m, c = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    startCity, endCity, dist = map(int, input().split())
    graph[startCity][endCity] = dist

for i in range(n+1):
    graph[i][i] = INF

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

cities = 0
time = -99999
for i in range(1, n+1):
    if graph[c][i] == INF or c == i: continue
    cities += 1
    if graph[c][i] > time:
        time = graph[c][i]

print(cities, time)