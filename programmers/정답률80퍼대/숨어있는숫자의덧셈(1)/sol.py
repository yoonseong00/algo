#문자열 사이에 있는 숫자를 찾아서 덧셈 연산
#문자를 하나씩 꺼내면 10이상인 수의 덧셈에 문제가 생기네... ㅅㅂ

def solution(my_string):

    number = ''

    answer = []

    for char in my_string:
        if char.isdigit():  #만약 문자가 숫자라면
            number += char  #임시 문자열에 추가
        else:
            if number:  #문자가 나오고 임시문자열에 값이 있으면 그 값을 answer에 추가
                answer.append(int(number))
                number = '' # 숫자를 answer에 넣었으면 number의 값을 지워야 다음 숫자와 충돌이 안생김
    
    if(number):
        answer.append(int(number))
    

    return sum(answer)

        

print(solution("aAb1B2cC34oOp"))