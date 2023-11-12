def solution(s):
    answer = 0
    count1 = 0
    count2 = 0

    s = list(s)

    for i in s:
        if count1 == count2:
            answer += 1
            string = i
        
        if i == string:
            count1 += 1
        else:
            count2 += 1

    return answer


print(solution("banana"))