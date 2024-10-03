'''
2 15
2
3

3 4
3
5
7

'''

############## 정석 풀이 ##############
# n은 화폐 개수, m은 구해야하는 액수
n, m = map(int, input().split())
moneyList = [int(input()) for _ in range(n)]

dpTable = [10001] * (m + 1)
dpTable[0] = 0

# 화폐 하나당 dp테이블 쫙~ 갱신해줌
for money in moneyList:
    for i in range(money, m+1):
        # 앞에 방법이 있었다면
        if not dpTable[i - money] == 10001:
            dpTable[i] = min(dpTable[i], dpTable[i - money] + 1)

print(dpTable[m] if not dpTable[m] == 10001 else -1)
######################################

############## 2024.10.03 ##############
# n, m = map(int, input().split())
# moneyList = [int(input()) for _ in range(n)]

# dpTable = [-1] * (10001)
# for money in moneyList:
#     dpTable[money] = 1

# for i in range(1, m+1):
#     for money in moneyList:
#         beforeAddThisMoney = i - money
#         if (beforeAddThisMoney) > 0 and not dpTable[beforeAddThisMoney] == -1:
#             if not dpTable[i] == -1 :
#                 dpTable[i] = min(dpTable[i], dpTable[beforeAddThisMoney]+1)
#             else:
#                 dpTable[i] = dpTable[beforeAddThisMoney]+1

# print(dpTable[m])
####################################