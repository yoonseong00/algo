def solution(food):

    answer = ''


    for idx, value in enumerate(food):
        for _ in range(value//2):
            answer += str(idx)

    reverse_name = ''

    for c in answer:
        reverse_name = c + reverse_name

    answer += '0'

    answer += reverse_name


    return answer

print(solution([1, 3, 4, 6]))