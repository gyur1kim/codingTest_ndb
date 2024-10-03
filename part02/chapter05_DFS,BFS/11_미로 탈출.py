'''
5 6
101010
111111
000001
111111
111111

'''


from collections import deque

############## 2024.10.02 ##############
N, M = map(int, input().split())  # N: 세로, M: 가로
maze = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def BFS(i, j, cnt):
    queue = deque([[i, j]])
    visited[i][j] = cnt

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == 1:
                if nx + 1 == N and ny + 1 == M:
                    return visited[x][y] + 1
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

print(BFS(0, 0, 1))
#######################################


############# 2022년의 나 ##################
# def BFS(x, y, cnt):
#     queue = deque([(x, y)])
#     visited[x][y] = cnt

#     while queue:
#         x, y = queue.popleft()
#         for d in range(4):
#             nx, ny = x + dx[d], y + dy[d]
#             if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == 1:
#                 if nx == N - 1 and ny == M - 1:
#                     return visited[x][y] + 1
#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append((nx, ny))


# N, M = map(int, input().split())  # N: 세로, M: 가로
# maze = [list(map(int, input())) for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# print(BFS(0, 0, 1))
####################################