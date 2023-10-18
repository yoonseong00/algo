def solution(keyinput, board):

    x = 0
    y = 0

    over_x = board[0] // 2
    over_y = board[1] // 2

    for i in keyinput:

        if i == 'left':
            x -= 1
        if i == 'right':
            x += 1
        if i == 'up':
            y += 1
        if i == 'down':
            y -= 1
        
        if x > over_x:
            x -= 1
        if x < (-over_x):
            x += 1
    
        if y > over_y:
            y -= 1
        if y < (-over_y):
            y += 1

    result = [x, y]




    return result

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))