numList = list(map(int, list(input())))
n = len(numList) // 2

print('LUCKY' if sum(numList[:n]) == sum(numList[n:]) else 'READY')