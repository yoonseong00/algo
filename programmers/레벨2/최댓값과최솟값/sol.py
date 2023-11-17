def solution(s):
    max_num= -100000000
    min_num=100000000

    s = s.split()

    for i in s:
        if int(i) > max_num:
            max_num = int(i)
        if int(i) < min_num:
            min_num = int(i)


    return f'{min_num} {max_num}'