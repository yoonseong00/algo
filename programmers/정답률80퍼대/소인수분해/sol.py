def solution(n):

    answer = []

    result = []

    num = 2

    while num <= n:
        if n % num == 0:
            result.append(num)
            n = n / num
        else:
            num = num + 1
    
    for i in result:
        if i not in answer:
            answer.append(i)

    return answer

print(solution(12))
print(solution(17))
print(solution(420))