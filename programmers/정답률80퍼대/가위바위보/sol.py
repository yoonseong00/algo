def solution(rsp):

    answer = ''

    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'


    return answer

# replace는 원본데이터를 건들이는 작업이기때문에 사용하기 힘듬

print(solution('2'))
print(solution('205'))