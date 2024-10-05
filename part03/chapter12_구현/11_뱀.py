# 보드의 크기
n = int(input())
board = [[0] * (n+1) for _ in range(n+1)]

# 사과의 개수
k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    board[row][col] = 9 # 사과를 보드에 위치시키자

# 뱀의 방향 변환 수
l = int(input())
timeDict  = dict()
for _ in range(l):
    # x시간 뒤 c방향으로 돌릴거다
    # L => 왼쪽으로 90도, D: 오른쪽으로 90도
    x, c = input().split()
    timeDict[int(x)] = c

# 상, 우, 하, 좌
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 현재 진행방향, 회전할 진행 방향, 현재 x값, 현재 y값
def rotate(currentD, to):
    # 왼쪽으로 돌거야
    if to == 'L':
        return 3 if currentD == 0 else currentD - 1
    return 0 if currentD  == 3 else currentD + 1

def move(currentD, x, y):
    nx, ny = direction[currentD]
    return (x+nx, y+ny)

def dummy():
    time = 0
    headX = 1
    headY = 1
    body = [(headX, headY)]
    board[headX][headY] = 1
    direct = 1

    while True:
        for i in range(n+1):
            print(board[i])
        print('============================')

        # 시간이 흘러
        time += 1

        # 이동한 머리의 위치
        nextHeadX, nextHeadY = move(direct, headX, headY)

        # 뱀 몸통이 있거나 벽이랑 부딪히면 땡
        if not 0 < nextHeadX <= n or not 0 < nextHeadY <= n: break
        if board[nextHeadX][nextHeadY] == 1: break

        # 현재 머리 위치를 하나 옮겨주자    
        headX = nextHeadX
        headY = nextHeadY
        body.append((headX, headY))

        
        # 머리 위치에 사과가 없으면 꼬리를 하나 옮긴당
        if not board[nextHeadX][nextHeadY] == 9:
            tailX, tailY = body.pop(0)
            board[tailX][tailY] = 0
        
        # 머리가 간 위치는 1로 바꾸자
        board[nextHeadX][nextHeadY] = 1

        if timeDict.get(time):
            print(timeDict.get(time))
            direct = rotate(direct, timeDict.get(time))
    
    return time

print(dummy())

        
        

