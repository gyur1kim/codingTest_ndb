'''
3 3
3 1 2
4 1 4
2 2 2

'''

# 각 행마다 가장 작은 값을 찾고, 그 값들 중 가장 큰 값을 찾으면 되는 문제.
# 입력 값이 최대 10,000으로 작기 때문에 기본 문법을 이용해 찾으면 됨
N, M = map(int, input().split())   # N은 행, M은 열
cards = [list(map(int, input().split())) for _ in range(N)]

res = 0
for row in cards:
    res = max(min(*row), res)
print(res)