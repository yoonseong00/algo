# 인덱스 번호가 짝수면 대문자로 출력
def solution(s):

    answer = ''

    s_list = s.split(' ')

    for i in s_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '

    return answer[0:-1]

print(solution("try hello world"))