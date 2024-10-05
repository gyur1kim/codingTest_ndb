'''
K1KA5CB7

AJKDLSI412K4JSJ9D

CBA

'''

n = list(input())
n.sort()

num = 0
answer = ''
for i in n:
    if i.isdigit(): # isDigit or isalpha
        num += int(i)
    else:
        answer += i

# 숫자가 아예 없는 케이스도 고려했어야 함

print(f'{answer}{num}' if num else f'{answer}')
