def solution(array, n):
    answer = 0

    for i in array:
        if i == n:
            answer += 1
        else:
            continue

    return answer

print(solution([1, 1, 2, 3, 4, 5], 1))