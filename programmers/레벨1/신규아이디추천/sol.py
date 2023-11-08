def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    #2
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i
    #3
    while True:
        if ".." in answer:
            answer = answer.replace("..",".")
        else:
            break
    #4
    if answer[0:1] == '.':
        answer = answer[1:]
    if answer[-1:0] == '.':
        answer = answer[:-1]
    #5
    if answer == '':
        answer = 'a'
    #6
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    #7
    while len(answer) < 3:
        answer += answer[-1]

    return answer
    


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
print(solution("=.="))
