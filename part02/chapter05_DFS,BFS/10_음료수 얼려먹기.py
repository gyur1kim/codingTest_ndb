'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

4 5
00110
00011
11111
00000

'''

N, M = map(int, input().split())
iceList = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


############ 모범답안 ################
def DFS(x, y, iceList):
    if not (0 <= x < N) or not (0 <= y < M) or iceList[x][y] == 1:
        return False
    
    iceList[x][y] = 1
    DFS(x, y - 1, iceList)
    DFS(x + 1, y, iceList)
    DFS(x, y + 1, iceList)
    DFS(x - 1, y, iceList)
    return True

answer = 0

for i in range(N):
    for j in range(M):
        if DFS(i, j, iceList):
            answer += 1

print(answer)
###################################


########## 2024.10.02의 나 ##########
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
# answer = 0

# def DFS(x, y, visited):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < N and 0 <= ny < M and iceList[nx][ny] == 0 and not visited[nx][ny]:
#             visited[nx][ny] = True
#             DFS(nx, ny, visited)

# for x in range(N):
#     for y in range(M):
#         if iceList[x][y] == 0 and not visited[x][y]:
#             answer += 1
#             DFS(x, y, visited)

# print(answer)
###################################


############# 2022년의 나 ##################
# '''
# DFS를 이용하면 해결할 수 있는 문제!
# 1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.
# 3. 1~2번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.
# '''
# def DFS(x, y):
#     stack = []
#     visited[x][y] = True
#     stack.append((x, y))

#     while stack:
#         x, y = stack.pop()
#         for d in range(4):
#             nx, ny = x+dx[d], y+dy[d]
#             if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and iceList[nx][ny] == 0:
#                 stack.append((nx, ny))
#                 visited[nx][ny] = True


# N, M = map(int, input().split())   # 세로 N, 가로 M
# iceList = [list(map(int, input())) for _ in range(N)]
# visited = [[False]*M for _ in range(N)]

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if iceList[i][j] == 0 and not visited[i][j]:
#             cnt += 1
#             DFS(i, j)
# print(cnt)
######################################