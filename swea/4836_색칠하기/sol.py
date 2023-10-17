import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    area = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input()) # N은 테스트케이스의 첫 줄에 칠할 영역의 개수

    count = 0

    for i in range(1, N+1):
        row1, col1, row2, col2, c olor = map(int, input().split())

        for row in range(row1, row2+1): # 행과열 생성
            for col in range(col1, col2+1):
                if color == 1: # 만약 빨갠색을 칠한다고 하면
                    if area[row][col] == 0: # 빈칸이면 빨간색으로 색칠
                        area[row][col] = 1
                    
                    elif area[row][col] == 2: # 파란색이면 보라색으로 칠하고 그 개수만큼 카운트
                        area[row][col] = 3
                        count += 1
                else:   # 파란색을 칠한다고 하면
                    if area[row][col] == 0: #빈칸이면 파란색으로 색칠
                        area[row][col] = 2
                    
                    elif area[row][col] == 1:   # 빨간색이면 보라색으로 칠하고 그 개수만큼 카운트
                        area[row][col] = 3
                        count += 1
    
    print(f'#{tc} {count}')