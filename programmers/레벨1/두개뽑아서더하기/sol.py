def solution(numbers):

    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    ans = sorted(set(answer))

    return ans

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))