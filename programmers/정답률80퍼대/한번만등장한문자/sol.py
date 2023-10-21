def solution(s):

    answer = ''
    
    for i in s:
        if s.count(i) == 1:
            answer += i

    ans = (''.join(sorted(answer)))

    return ans

print(solution("aaabbbbcccd"))