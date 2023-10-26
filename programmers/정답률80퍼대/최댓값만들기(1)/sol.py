def solution(numbers):

    ans = sorted(numbers, reverse=True)

    answer = ans[0] * ans[1]

        
    return answer

print(solution([1,2,4,3,5]))
print(solution([0, 31, 24, 10, 1, 9]))