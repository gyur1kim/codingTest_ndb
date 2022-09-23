'''
5 8 3
2 4 5 4 6

'''
'''
가장 큰 수와 두 번째로 큰 수만 고려하면 된다.
'''
N, M, K = map(int, input().split())  # 배열의 크기 N, 숫자가 더해지는 횟수 M, 최대 더할 수 있는 횟수 K
data = list(map(int, input().split()))
data.sort(reverse=True)

# 직관적인 풀이지만, M이 100억이면 시간 초과 판정을 받을 것이다.
'''
ans = 0
for n in range(1, M+1):
    ans += data[0] if n % (K+1) else data[1]
print(ans)
'''

# 반복되는 수열에 대해 파악하자!!!!!
ans = (data[0] * K + data[1]) * (M//(K+1)) + (data[0] * (M % (K+1)))
print(ans)