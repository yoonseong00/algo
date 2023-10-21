def solution(sides):

    side = sorted(sides)

    if side[0] + side[1] > side[2]:
        return 1
    else:
        return 2

print(solution([1,2,3]))