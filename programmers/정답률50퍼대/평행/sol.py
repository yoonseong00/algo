# 평행의 조건
# 1. 기울기 동일(직교)
# 2. y절편이 달라야 함 인데... y 절편..? 일단 없다고 가정 ㄱ

# 기울기 구하기
# 3번을 반복해야하니까 함수로 만들기
def giulgi(dot1, dot2):
    
    giulgi = (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])

    return giulgi 

def solution(dots):

    result = 0
    
    # 기울기가 동일하다 = 직교다 곧, 평 행
    if giulgi(dots[0], dots[1]) == giulgi(dots[2], dots[3]):
        result = 1
    
    if giulgi(dots[0], dots[2]) == giulgi(dots[1], dots[3]):
        result = 1
    
    if giulgi(dots[0], dots[3]) == giulgi(dots[1], dots[2]):
        result = 1
    
    return result



print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))