def solution(n, numlist):

    answer = []

    for num in numlist:
        if num % n == 0:
            answer.append(num)

    return answer

print(solution(3, [4,5,6,7,8,9,10,11,12]))