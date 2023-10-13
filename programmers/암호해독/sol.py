def solution(cipher, code):

    answer = ''

    for i in range(code, len(cipher)+1):
        if i % code == 0:
            answer +=cipher[i-1]

    return answer

print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))