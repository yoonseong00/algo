def solution(dots):
    
    dot = sorted(dots)

    area = (dot[3][0] - dot[0][0]) * (dot[3][1] - dot[0][1])      
    
    return area

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]	))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]	))