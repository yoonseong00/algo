def solution(s):
    
    ans = list(s)

    count = 0

    for i in ans:
        if i == 'p' or i== 'P':
            count += 1
        elif i == 'y' or i =='Y':
            count -= 1
    
    if count == 0:
        return True
    else:
        return False