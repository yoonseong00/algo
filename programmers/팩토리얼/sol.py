def solution(n):

    result = 1
    answer = 1

    while result <= n:
        answer += 1

        result = result * answer

    answer = answer - 1
        
  
    return answer

print(solution(7))
print(solution(3628800))
