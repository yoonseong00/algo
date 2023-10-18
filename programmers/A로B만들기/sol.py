def solution(before, after):

    a = before

    for i in before:
        if i in after:
            a = a.strip(i)
        if len(a) > 0:
            return 0
        else:
            return 1


    
   

print(solution("olleh", "hello"))