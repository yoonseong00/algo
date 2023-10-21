def solution(emergency):

    sorted_nums = sorted(emergency, reverse=True)
    answer = []
    
    for i in emergency:
        answer.append(sorted_nums.index(i)+1)

    return answer

print(solution([1,2,3,4,5,6]))