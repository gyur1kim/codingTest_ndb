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

# 시작점이 있다.
# 한 번 돌때마다 현재 가장 길이가 짧은 노드를 찾아야한다.
# 노드 길이 정보를 저장하는 리스트가 필요하다.
# visited를 통해 이미 방문한 노드는 계산하지 않아야 한다.
# 최단 경로의 핵심은 "인접한 노드들아~ 나를 거쳐가는게 빠르니 아니면 기존이 빠르니"를 비교하는 것이다.

import sys
input = sys.stdin.readline
INF = int(1e9)

n, v = map(int, input().split()) # 노드, 간선
start = int(input())             # 시작점

# 1 2 2 -> 1에서 2로 가는 간선의 길이는 2라는 뜻
graph = [[] for _ in range(n+1)]
for _ in range(v):
    nodeFrom, nodeTo, length = map(int, input().split())
    graph[nodeFrom].append((nodeTo, length))

# 최단거리를 저장할 리스트
distance = [INF] * (n + 1)

# 방문 여부를 저장할 리스트
visited = [False] * (n + 1)

def getShortestNode():
    idx = 0
    minValue = INF

    for i in range(1, n+1):
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            idx = i
    
    return idx

print(graph)

def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    for nodeTo, length in graph[start]:
        # 일단 시작 노드에 연결된 노드들의 distance 입력(INF보다 더 가까운 거리를 찾았자나~)
        distance[nodeTo] = length
    
    # 이제 노드 n-1개(시작노드 제외) 전체 돌아보자
    for _ in range(n-1):
        # 현재 기준 가장 짧고, 방문하지 않은 노드를 찾아
        currentNode = getShortestNode()
        visited[currentNode] = True

        # 이 노드들이 연결된 다음 노드들에 대해서 dist값 갱신해주자
        for nodeTo, length in graph[currentNode]:
            # nodeTo로 갈 때, 기존의 distance값이 더 빠른가? 아니면 나를 거쳐가는 게 더 빠른가?
            cost = length + distance[currentNode]
            if cost < distance[nodeTo]:
                distance[nodeTo] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('Infinity', end=" ")
    else:
        print(distance[i], end=" ")



