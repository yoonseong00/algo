def solution(arr):

    if len(arr) == 1:
        return [-1]

    min_num = min(arr)
    arr.remove(min_num)
    
    return arr

print(solution([4,3,2,1]))