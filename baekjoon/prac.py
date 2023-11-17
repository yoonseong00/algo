def solution(wallpaper):
    rows = len(wallpaper)
    cols = len(wallpaper[0])

    top_left_x = 100000000
    top_left_y = 10000000000
    bottom_right_x = 0
    bottom_right_y = 0
    print(bottom_right_x)

    for i in range(rows):
        for j in range(cols):
            if wallpaper[i][j] == '#':
                top_left_x = min(top_left_x, j)
                top_left_y = min(top_left_y, i)
                bottom_right_x = max(bottom_right_x, j)
                bottom_right_y = max(bottom_right_y, i)

    return [top_left_y, top_left_x, bottom_right_y, bottom_right_x]

print(solution([".#...", "..#..", "...#."]	))