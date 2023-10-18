def solution(array):
    count = [0] * (max(array)+1)

    for i in array:
        count[i] += 1

    num = 0
    for c in count:
        if c == max(count):
            num += 1
    
    if num > 1:
        return -1
    else:
        return count.index(max(count))
        
    
    return num

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]	))
print(solution([1]))