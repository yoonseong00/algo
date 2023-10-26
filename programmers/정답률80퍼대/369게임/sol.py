def solution(order):

    count = 0
    
    for i in str(order):
        if i in ['3', '6', '9']:
            count += 1

    return count
        


print(solution(3))
print(solution(29423))