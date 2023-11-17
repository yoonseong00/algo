def solution(myString):
    answer = ''
    for i in myString:
        if i.islower():
            answer += i
        else:
            answer += i.lower()
    return answer