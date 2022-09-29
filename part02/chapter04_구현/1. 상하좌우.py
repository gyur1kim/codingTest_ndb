'''
5
R R R U D D

'''

N = int(input())
go = list(input().split())


# 그냥 입력받아 푸는 방법
'''
visitor = [1, 1]
for order in go:
    if order == 'U':
        if visitor[0] -1 > 0:
            visitor[0] -= 1
    elif order == 'D':
        if visitor[0] +1 <= N:
            visitor[0] += 1
    elif order == 'L':
        if visitor[1] -1 > 0:
            visitor[1] -= 1
    elif order == 'R':
        if visitor[1] +1 <= N:
            visitor[1] += 1
print(*visitor)
'''


# 델타 탐색을 이용해 풀기
'''
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveTypes = ['L', 'R', 'U', 'D']
for order in go:
    for i in range(4):
        if order == moveTypes[i]:
            nx = dx[i]
            ny = dy[i]
            if 0<x+nx<=N and 0<y+ny<=N:
                x, y = x+nx, y+ny
print(x, y)
'''

# 델타탐색 응용 - 내가 생각해냈음!!
x, y = 1, 1

moveTypes = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
for order in go:
    nx, ny = moveTypes[order]
    if 0<x+nx<=N and 0<y+ny<=N:
        x, y = x+nx, y+ny
print(x, y)