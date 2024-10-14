def solution(n, build_frame):
    answer = []
    
    def isPossible():
        for x, y, stuff in answer:
            # 기둥이면
            if stuff == 0:
                # 바닥위      보의 왼쪽                 보의 오른쪽              기둥 위
                if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                    continue
                else:
                    return False
            # 보면
            else:  
                #  보의 왼쪽에 기둥            보의 오른쪽에 기둥           다른 보와 연결됨
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                    continue
                else:
                    return False
        return True
            

    for x, y, stuff, type in build_frame:
        # 삭제하자궁~
        if type == 0:
            answer.remove([x, y, stuff])
            if not isPossible(): answer.append([x, y, stuff])
        # 넣어보자공
        else:
            answer.append([x, y, stuff])
            if not isPossible(): answer.pop()
    
    return sorted(answer)