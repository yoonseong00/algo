def solution(s):

    answer = []

    eng = list(s)

    dae = []
    so = []


    for i in eng:
        if i.isupper():
            dae.append(i)
        else:
            so.append(i)
    
    a = sorted(dae, reverse = True)
    b = sorted(so, reverse = True)
    

    answer = b + a

    return ''.join(answer)

            

print(solution("Zbcdefg"))