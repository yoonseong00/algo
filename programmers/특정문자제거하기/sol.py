# def solution(my_string, letter):
    
#     answer = ''                                   #replace method를 사용해서 letter 부분을 띄어쓰기 처리하기

#     answer = my_string.replace(letter,'') 
        
#     return answer

def solution(my_string, letter):
    answer = ''

    for string in my_string:
        if string != letter:                    #특정한 문자를 제외하고 나머지를 출력(합한다)
            answer += string

    return answer



print(solution('abcdef', 'f'))