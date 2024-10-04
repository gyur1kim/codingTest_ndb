'''
3 2 1
1 2 4
1 3 2

'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시 개수 n, 통로 개수 m, 메시지를 보내고자 하는 도시 c
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    startCity, endCity, dist = map(int, input().split())
    graph[startCity].append((dist, endCity))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, city = heapq.heappop(q)
        if dist > distance[city]: continue

        for nextDist, nextCity in graph[city]:
            cost = distance[city] + nextDist
            if cost < distance[nextCity]:
                distance[nextCity] = cost
                heapq.heappush(q, (cost, nextCity))

dijkstra(c)

cities = 0
time = 0
for dist in distance:
    if dist == INF or dist == 0: continue
    cities += 1
    time = max(time, dist)

print(cities, time)



################ 플로이드 워셜 ################
# INF = int(1e9)

# # 도시 개수 n, 통로 개수 m, 메시지를 보내고자 하는 도시 c
# n, m, c = map(int, input().split())

# graph = [[INF] * (n+1) for _ in range(n+1)]
# for _ in range(m):
#     startCity, endCity, dist = map(int, input().split())
#     graph[startCity][endCity] = dist

# for i in range(n+1):
#     graph[i][i] = INF

# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# cities = 0
# time = -99999
# for i in range(1, n+1):
#     if graph[c][i] == INF or c == i: continue
#     cities += 1
#     if graph[c][i] > time:
#         time = graph[c][i]

# print(cities, time)
##############################################