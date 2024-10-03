'''
4 6
19 15 10 17

'''

############# 2024.10.03 ################
n, m = map(int, input().split())
tteok = list(map(int, input().split()))

def cutTteok(list, target, start, end):
    height = 0

    while start <= end:
        mid = (start + end) // 2
        cuttedTteok = 0

        for t in list:
            if t > mid:
                cuttedTteok += t - mid

        if cuttedTteok == target:
            return height
        elif cuttedTteok < target:
            end = mid - 1
        else:
            # 이 경우에 떡을 줄 수 있으므로 여기에 height를 갱신해줘야함
            height = mid
            start = mid + 1

    return height

# 가장 큰 값을 찾으려면, 굳이 정렬하지 않고 max(tteok)해도 된대
# tteok.sort()
print(cutTteok(tteok, m, 0, tteok[n-1]))
##########################################
