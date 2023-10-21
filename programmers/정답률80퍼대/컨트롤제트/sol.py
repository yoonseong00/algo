def solution(s):
    answer = s.split()

    num = 0

    for i in range(len(answer)):
        if answer[i] == 'Z':
            num -= int(answer[i-1])
        else:
            num += int(answer[i])

    return num

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("-1 -2 -3 Z"))