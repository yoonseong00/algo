def solution(park, routes):
    x = 0
    y = 0 
    # 시작지점
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = j
                y = i
                break
    # 산책을 떠나보자
    for route in routes:
        # 스타트지점
        sx = x
        sy = y
        for walk in range(int(route[2])):
            if route[0] == 'E' and sx != len(park[0])-1 and park[sy][sx+1] != 'X':
                sx += 1
                if walk == int(route[2])-1:
                    x = sx
            elif route[0] == 'W' and sx != 0 and park[sy][sx-1] != 'X':
                sx -= 1
                if walk == int(route[2])-1:
                    x = sx
            elif route[0] == 'S' and sy != len(park[0])-1 and park[sy+1][sx] != 'X':
                sy += 1
                if walk == int(route[2])-1:
                    y = sy
            elif route[0] == 'N' and sy != 0 and park[sy-1][sx] != 'X':
                sy -= 1
                if walk == int(route[2])-1:
                    y = sy

    return [y,x]


print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))