def solution(num, k):


    number = list(map(int, str(num)))

    if k in number:
        return number.index(k)+1
    else:
        return -1


print(solution(29183, 1))
print(solution(232443, 4))
