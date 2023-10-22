def solution(array):

    str_array = str(array)

    answer = 0

    for i in str_array:
        answer += i.count('7')

    return answer
    
    

print(solution([7,77,777]))