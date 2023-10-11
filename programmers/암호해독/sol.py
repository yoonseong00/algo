def solution(cipher, code):

    answer = ''

    for ci in range(1, len(cipher)):
       if ci % 4 == 0:
        # answer += cipher(ci)


    return answer

print(solution("dfjardstddetckdaccccdegk", 4))