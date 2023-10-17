def solution(n):
    
    answer = 0
    
    for i in range(1, n+1):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

print(solution(15))

# 이 문제의 핵심 : 3은 그냥 어디에도 죽어도 있으면 안됨