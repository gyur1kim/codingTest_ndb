'''
a1

'''

posCol, posRow = input()
posCol = ord(posCol)-ord('a')   # 열
posRow = int(posRow)            # 행

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]
cnt = 0
for step in steps:
    nx, ny = step
    if 0<=posCol+ny<8 and 0<posRow+nx<=8:
        cnt += 1
print(cnt)