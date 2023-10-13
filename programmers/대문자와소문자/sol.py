def solution(my_string):

    answer = ''

    for r in my_string:
        # print(r)
        if r.islower():
            answer += r.upper()
        else:
            answer += r.lower()

    return answer

print(solution('cccCCC'))