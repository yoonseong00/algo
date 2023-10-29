def solution(d, budget):

    don = sorted(d)

    while sum(don) > budget:
        don.pop()

    return len(don)