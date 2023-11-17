def solution(s):
    answer = ''
    result = ''
    for i in s:
        if not answer:
            answer += i.upper()
        else:
            answer += i.lower()
        if i == ' ':
            result += answer
            answer = ''

    result += answer
    
    return result

print(solution("3people unFollowed me"))