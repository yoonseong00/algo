def solution(x):
    arr = list(str(x))
    sum_x = 0

    for i in range(len(arr)):
        sum_x += int(arr[i])
        if x % sum_x == 0:
            answer = True
        else:
            answer = False

    return answer

print(solution(20))
