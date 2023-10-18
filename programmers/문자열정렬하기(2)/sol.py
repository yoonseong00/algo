def solution(my_string):

    answer = sorted(my_string.lower())

    result = ''.join(answer)

    return result

print(solution("Bcad"))