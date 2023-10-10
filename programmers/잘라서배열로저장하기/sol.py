def solution(my_str, n):

    # answer = [my_str[i:i+n] for i in range(0, len(my_str), n)] 
    
    answer = []

    for i in range(0, len(my_str), n):
        print(i)
        answer.append(my_str[i:n+i])

    return answer

print(solution("abc1Addfggg4556b", 6))