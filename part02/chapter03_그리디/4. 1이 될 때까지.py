'''
25 3

'''

# 그냥 열심히 나누고 더해보자규
N, K = map(int, input().split())
res = 0
while True:
    N, m = divmod(N, K)
    res += (m + 1)
    if N == 1:
        break
    elif N == 0:
        res -= 2
        break
print(res)

'''
주어진 N에 대하여 최대한 많이 나누기를 수행하면 된다.
K가 2 이상이기만 하면 K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N의 값을 줄일 수 있으며, N이 결국 1에 도달한다.
그러므로 K로 최대한 많이 나눌 수 있도록 하는 것이 최적의 해를 보장한다.
'''