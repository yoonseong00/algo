def solution(a, b, n):

    answer = 0

    while n >= a:
        count = n % a

        n = (n//a) * b

        answer += n

        n += count
   
    return answer

print(solution(2,1,20))