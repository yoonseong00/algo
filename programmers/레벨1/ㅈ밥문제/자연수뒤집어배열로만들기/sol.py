def solution(n):
    answer = []
    n = str(n)
    for i in n:
        i=int(i) 
        answer.append(i)
    answer.reverse() 
    return answer