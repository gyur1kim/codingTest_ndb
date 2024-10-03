'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

'''

# 리스트보다 빠름.
# 가장 짧은 노드 찾기 + 방문 여부 => 힙큐, distance리스트로 관리 가능
# 핵심은 여전히 "다음 노드들이 나를 거쳐가는 게 빠른지 기존이 빠른지?"임

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, v = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(v):
    fromN, toN, dist = map(int, input().split())
    graph[fromN].append((dist, toN))

distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, currentNodeIdx = heapq.heappop(q)

        if dist > distance[currentNodeIdx]:
            continue

        for nextNodeDist, nextNodeIdx in graph[currentNodeIdx]:
            cost = distance[currentNodeIdx] + nextNodeDist
            if cost < distance[nextNodeIdx]:
                distance[nextNodeIdx] = cost
                heapq.heappush(q, (cost, nextNodeIdx))

dijkstra(start)

for i in range(1, n+1):
    print('INF' if distance[i] == INF else distance[i], end=" ")


##########################################################
# import sys
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)

# # 노드, 간선
# n, v = map(int, input().split())
# start = int(input())

# # 그래프
# graph = [[] for _ in range(n + 1)]
# for _ in range(v):
#     nodeFrom, nodeTo, dist = map(int, input().split())
#     # 힙큐는 맨 앞에거 기준으로 뱉음
#     # 최단거리를 구하고 있으므로 dist를 앞에 두자
#     graph[nodeFrom].append((dist, nodeTo))

# # 최단거리 관리 리스트
# distance = [INF] * (n + 1)

# # node는 (dist, to) 로 관리합니다 주의주의
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0

#     while q:
#         print(q)
#         dist, current = heapq.heappop(q)
        
#         # 방문한 적 없는 녀석만... 진행
#         if dist > distance[current]:
#             continue

#         # nexttNode = (dist, node)를 갖는다
#         for 다음 in graph[current]:
#             # 나를 거쳐가는 경우
#             cost = dist + 다음[0]
#             if cost < distance[다음[1]]:
#                 distance[다음[1]] = cost
#                 heapq.heappush(q, (cost, 다음[1]))


# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print('INFINITY')
#     else: print(distance[i])
##########################################################