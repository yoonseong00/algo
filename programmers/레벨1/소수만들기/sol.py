import itertools

def sosu(x):
    if x < 2:
        return False
    for j in range(2, int(x**(1/2))+1):
        if x % j == 0:
            return False
    
    return True


def solution(nums):
    answer = 0

    arr = list(itertools.combinations(nums, 3))

    for num in arr:
        if sosu(sum(num)):
            answer += 1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))