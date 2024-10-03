'''
5
8 3 7 9 2
3
5 7 9

'''

import sys

############# 반복문 구현 ##############
n = int(sys.stdin.readline().rstrip())
toolList = list(map(int, sys.stdin.readline().rstrip().split()))
toolList.sort()
k = int(sys.stdin.readline().rstrip())
customerNeed = list(map(int, sys.stdin.readline().rstrip().split()))

def binarySearch(list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

for customer in customerNeed:
    print('yes' if binarySearch(toolList, customer, 0, n - 1) else 'no', end=' ')
#######################################

############## 2024.10.03 ################
# 재귀
# n = int(sys.stdin.readline().rstrip())
# toolList = list(map(int, sys.stdin.readline().rstrip().split()))
# toolList.sort()
# k = int(sys.stdin.readline().rstrip())
# customerNeed = list(map(int, sys.stdin.readline().rstrip().split()))

# def binarySearch(list, target, start, end):
#     if start > end:
#         return False
#     mid = (start + end) // 2

#     if list[mid] == target:
#         return True
#     elif list[mid] > target:
#         return binarySearch(list, target, start, mid - 1)
#     else:
#         return binarySearch(list, target, mid + 1, end)

# for customer in customerNeed:
#     print('yes' if binarySearch(toolList, customer, 0, n - 1) else 'no', end=' ')
####################################