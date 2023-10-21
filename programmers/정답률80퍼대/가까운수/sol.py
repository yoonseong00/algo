def solution(array, n):

    sort_num = sorted(array)

    answer = 0
    
    near_num = 10000000

    for i in sort_num:
        if near_num != abs(n - i):
            if near_num > abs(n - i):
                near_num = abs(n - i)
                answer = i 
    
    return answer

        

print(solution([3, 10, 28], 20))
print(solution([10, 11, 12,14],13))