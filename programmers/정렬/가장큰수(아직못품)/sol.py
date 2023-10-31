import itertools

def solution(numbers):

    n = int(len(numbers))

    num_list = itertools.combinations(numbers, n)


    answer = ''

    for i in num_list:
        print(i)
        num = ''
        max_num = 0
        for j in range(len(numbers)):
            num += str(j)
        print(num)
        if int(num) > max_num:
            max_num = int(num)

    return max_num

print(solution([6, 10, 2]))