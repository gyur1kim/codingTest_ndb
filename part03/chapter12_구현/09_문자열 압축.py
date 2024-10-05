# def solution(s):
#     def ifDifferent(result, cnt, str):
#         if cnt > 1:
#             result += f'{cnt}{str}'
#         else:
#             result += str
#         return result
    
#     answer = len(s)
    
#     # 1부터 잘라보겠슴당~
#     for i in range(1, len(s) // 2 + 1):
#         textList = []
#         for j in range(0, len(s), i):
#             divided = s[j:j+i]
#             textList.append(divided) 
        
#         cnt = 1
#         result = ''
#         for index in range(1, len(textList)):
#             prevStr = textList[index-1]
#             currentStr = textList[index]
#             if prevStr == currentStr:
#                 cnt += 1
#             else:
#                 result = ifDifferent(result, cnt, prevStr)
#                 cnt = 1
#             # 마지막 인덱스에 대해 처리하기
#             if index == len(textList) - 1:
#                 result = ifDifferent(result, cnt, currentStr)
        
#         answer = min(answer, len(result))
            
#     return answer


### 프로그래머스 따봉많은 풀이
# zip을 이용해 원본 + 하나씩 밀린 애들로 비교한다
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    print(res)
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    'aaaaaa',
]

for x in a:
    print(solution(x))