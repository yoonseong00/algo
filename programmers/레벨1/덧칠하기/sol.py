# n	m	section	result
# 8	4	[2, 3, 6]	2
# 5	4	[1, 3]	1
# 4	1	[1, 2, 3, 4]	4

def solution(n, m, section):
    answer = 0
    while section:
        draw = section[0] + m
        while section and section[0] < draw:
            section.pop(0)
            
        answer+=1
    
    return answer

print(solution(8,4,[2, 3, 6]))