def solution(before, after):

    str_list = list(map(str, after))

    for i in before:
        if i in str_list:
            str_list.remove(i)

    if len(str_list) == 0:
        return 1
    else:
        return 0


print(solution("olllh", "hello"))