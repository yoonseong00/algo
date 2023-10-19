def solution(numbers):

    numbers.sort()

    return max(numbers[0]* numbers[1], numbers[-1]*numbers[-2])

print(solution([1, 2, -3, 4, -5]))