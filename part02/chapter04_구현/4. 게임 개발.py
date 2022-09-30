'''
5 5
1 1 0
1 1 1 1 1
1 0 1 1 1
1 0 0 0 1
1 1 0 0 1
1 1 1 1 1

'''

'''
1. 현재 위치를 방향을 기준으로 반시계방향으로 90도씩 회전하며 갈 곳 결정하기.
2. 탐색 중, 가보지 않은 길이 있으면 왼쪽으로 회전 후 전진하기
   가본 길이면 다시 왼쪽으로 돌기
3. 다 가본 곳이면 방향을 유지한 채 한 칸 뒤로 간다. 뒤에가 바다면 탐색 종료
'''

N, M = map(int, input().split())     # 세로 크기 N, 가로 크기 M
x, y, d = map(int, input().split())  # 캐릭터가 북쪽으로부터 떨어진 거리, 서쪽으로부터 떨어진 거리
                                     # 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽  -> 이걸 인덱스로 쓰네
area = [list(map(int, input().split())) for _ in range(N)]  # 0: 육지, 1: 바다

# 내가 작성한 코드
def search(x, y, d):
    global cnt
    visited[x][y] = True
    turnCnt = 0
    while turnCnt < 4:
        nx, ny = x + direction[d][0], y + direction[d][1]
        if not visited[nx][ny] and area[nx][ny] == 0:
            cnt += 1
            search(nx, ny, d)
        else:
            d = d-1 if d-1 >= 0 else 3
        turnCnt += 1


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북쪽, 동쪽, 남쪽, 서쪽
visited = [[False]*M for _ in range(N)]         # 캐릭터가 방문한 곳 표시하기

cnt = 1
search(x, y, d)
print(cnt)



# 책 예제코드
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북쪽, 동쪽, 남쪽, 서쪽
visited = [[False]*M for _ in range(N)]         # 캐릭터가 방문한 곳 표시하기
visited[x][y] = True

def turnLeft():
    global d
    d -= 1
    if d == -1:
        d = 3


count = 1
turnTime = 0
while True:
    turnLeft()
    nx, ny = x + direction[d][0], y + direction[d][1]

    if not visited[nx][ny] and area[nx][ny] == 0:
        visited[nx][ny] = True
        x = nx
        y = ny
        count += 1
        turnTime = 0
        continue
    else:
        turnTime+= 1

    if turnTime == 4:
        nx, ny = x - direction[d][0], y - direction[d][1]
        if area[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turnTime = 0
print(count)