def solution(money):

    a = money // 5500
    b = money - a*5500

    answer = [a, b]
    
    
    return answer

print(solution(5500))
print(solution(15000))