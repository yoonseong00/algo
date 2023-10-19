def solution(polynomial):
    poly = polynomial.replace(' ','').split('+')
    
    x = 0
    y = 0

    for i in poly:
        if 'x' in i:
            if len(i) > 1:
                x += int(i[:-1])
            else:
                x += 1
        else:
            y += int(i)
    
    if x == 0:
        return f'{y}'
    elif x == 1:
        if y == 0:
            return f'x' # {x}로 만들게 되면  1*x일때 문제생김... 아니 ㅅㅂ 왜 이게 문젠데
        else:
            return f'x + {y}'
    elif x > 1:
        if y == 0:
            return f'{x}x'
        else:
            return f'{x}x + {y}'
        

print(solution("3x + 7 + x"))