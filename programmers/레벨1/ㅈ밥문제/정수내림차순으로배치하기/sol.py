def solution(n):

    answer = sorted(str(n), reverse = True)

    result = ''

    for i in answer:
        result += i

    return int(result)


print(solution(118372))