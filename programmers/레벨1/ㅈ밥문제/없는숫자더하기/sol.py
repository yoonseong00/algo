def solution(numbers):

    answer = []

    for i in range(10):
        if i not in numbers:
            answer.append(i)
        
    return sum(answer)

print(solution([1,2,3,4,6,7,8,0]))