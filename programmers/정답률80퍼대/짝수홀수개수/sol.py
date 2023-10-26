def solution(num_list):

    x = 0
    y = 0

    for i in num_list:
        if i % 2 ==0:
            x += 1
        else:
            y +=1
    
    answer = [x, y]
    
    return answer

print(solution([1,2,3,4,5]))
print(solution([1, 3, 5, 7]))