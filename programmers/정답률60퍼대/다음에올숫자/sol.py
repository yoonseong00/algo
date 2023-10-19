def solution(common):
    if common[1] - common[0] == common[-1] - common[-2]:    #등차
        a = common[-1] + (common[1] - common[0])
        return a

    else:   #등비
        b = common[-1] * (common[-1] // common[-2])
        return b
        
        

    
print(solution([1,2,3,4]))