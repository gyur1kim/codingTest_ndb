'''
5

'''

'''
복잡해보이지만 그렇지 않은 문제다!
왜냐면 하루는 86400초기 때문에 파이썬은 금방 해결해낼 수 있다.

완전탐색 문제 -> 데이터의 개수가 100만 이하일 때 사용한다.
'''

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)