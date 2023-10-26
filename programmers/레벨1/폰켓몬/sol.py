def solution(nums):
    
    nums_len = len(set(nums))   # nums에서 중복된 숫자 없애기
    num = len(nums) / 2 # 절반만 가져가는 상황

    if num < nums_len:
        answer = num
    else:
        answer = nums_len
    
    return int(answer)


print(solution([3,1,2,3]))