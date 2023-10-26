import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n):

    answer = ''

    a = convert(n, 3)

    a_a = list(a)

    while len(a_a) > 0:
        answer += a_a[-1]
        a_a.pop()

    return int(answer, 3)


print(solution(45))