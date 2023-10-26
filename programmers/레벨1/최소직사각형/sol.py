def solution(sizes):

    a = []
    b = []

    for c in sizes:
        if c[0] > c[1]:
            a.append(c[0])
            b.append(c[1])
        else:
            a.append(c[1])
            b.append(c[0])     

    return max(a) * max(b)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

