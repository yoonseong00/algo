# def solution(numbers, num1, num2):
    
#     answer = []

#     answer = numbers[num1: num2+1]
    
#     return answer

def solution(numbers, num1, num2):
    
    answer = []

    for num in range(num1, num2+1):
        answer.append(numbers[num])
    
    return answer

print(solution([1, 2, 3, 4, 5], 1, 3))
print(solution([1, 3, 5], 1, 2))