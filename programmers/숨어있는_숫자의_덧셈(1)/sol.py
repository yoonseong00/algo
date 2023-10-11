import re

# def solution(my_string):

    num = re.sub(r'[^0-9]', '', my_string)

    n = list(map(int, num))

    answer = sum(n)
        

    return answer

#region Description 선생님 예시(파이썬 안의 함수 사용)
# def solution(my_string):

    answer = 0

    for char in my_string:
        if char.isdight():
            answer += int(char)
        

    return answer
#endregion Description 
    

#region Description 선생님 예시 2(try문 사용)
def solution(my_string):


    answer = 0

    for char in my_string:
            try:
                answer += int(char)
            except:
                continue
        
    return answer
#endregion Description 


#region Description 선생님 예시3(아스키코드이용)

def solution(my_string):

    answer = 0

    for char in my_string:
        if not ((ord('A') <= ord(char) <=ord('z'))):
            answer += int(char)
        

    return answer
#endregion Description 
print(solution("aAb1B2cC34oOp"))