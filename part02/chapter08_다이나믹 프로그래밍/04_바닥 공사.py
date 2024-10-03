'''
3

'''

# 타일 사이즈는 2*1, 1*2, 2*2 세 종류
n = int(input())

dpTable = [0] * 1001
dpTable[1] = 1
dpTable[2] = 3

for i in range(3, n+1):
    dpTable[i] = (dpTable[i-1] + 2 * dpTable[i-2]) % 796796

print(dpTable[n]) 