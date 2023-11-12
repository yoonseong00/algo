# 핵심: 빵 - 아채 - 고기 - 빵이 나와야 완성
# 1: 빵, 2:야채, 3: 고기
# 1 2 3 1 -> 하나의 묶음

def solution(ingredient):
    hambuger = []

    answer = 0

    for i in ingredient:
        hambuger.append(i)
        if hambuger[-4:] == [1,2,3,1]:
            answer += 1
            hambuger.pop()
            hambuger.pop()
            hambuger.pop()
            hambuger.pop()
    
    return answer

