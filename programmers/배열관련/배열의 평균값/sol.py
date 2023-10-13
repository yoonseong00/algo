def solution(numbers):
    sum = 0 
    
    for i in numbers:
        sum += i 
    
    answer = sum / len(numbers)


    return answer

print(solution([1,2,3,4,5]))