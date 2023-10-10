def solution(my_string, letter):
    
    answer = my_string

    for char in my_string:
        if char in letter:
            answer = answer.replace(char, '')
        
    return answer

print(solution('abcdef', 'f'))