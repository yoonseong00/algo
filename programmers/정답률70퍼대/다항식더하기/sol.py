# def solution(polynomial):
#     poly = polynomial.replace(' ','').split('+')
    
#     x = 0
#     y = 0

#     for i in poly:
#         if 'x' in i:
#             if len(i) > 1:
#                 x += int(i[:-1])
#             else:
#                 x += 1
#         else:
#             y += int(i)
    
#     if x == 0:
#         return f'{y}'
#     elif x == 1:
#         if y == 0:
#             return f'x' # {x}로 만들게 되면  1*x일때 문제생김... 아니 ㅅㅂ 왜 이게 문젠데
#         else:
#             return f'x + {y}'
#     elif x > 1:
#         if y == 0:
#             return f'{x}x'
#         else:
#             return f'{x}x + {y}'



def solution(polynomial):
    num = 0     # 7
    strr = 0    # ' x'
    polynomial = polynomial.split('+') # ['3x ', ' 7 ', ' x'], ['x ', ' x ', ' x']

    for i in polynomial:
        term = i.strip()
        if term.isdigit():
            num += int(term)
        else:
            if term == 'x':
                strr += 1
            else:
                strr += int(term[:-1])
    if strr == 0:
        return str(num)
    elif strr == 1:
        if num == 0:
            return 'x'
        else:
            return f'x + {str(num)}'
    else:
        if num != 0:
            return f'{strr}x + {num}'
        else:
            return f'{strr}x'

print(solution("3x + 7 + x"))

print(solution('x + 1'))