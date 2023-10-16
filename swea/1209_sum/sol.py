import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc = int(input())
    matrix = []

    max_sum = 0

    # _ => 변수를 활용하지 않겠다 할 때 사용
    for _ in range(100):
        numbers = list(map(int,(input().split())))

        matrix.append(numbers)


    # 가로줄
    for row in range(len(matrix)):
        total = 0
        for col in range(len(matrix[0])):
            total += matrix[row][col]
        if max_sum < total:
            max_sum = total

    # 세로줄
    for col in range(100):
        total = 0
        for row in range(100):
            total += matrix[row][col]
        if max_sum < total:
            max_sum = total
    # 좌상단 => 우하단 대각선
    total = 0
    for i in range(100):
        total += matrix[i][i]
        if max_sum < total:
            max_sum = total
    # 우상단 => 좌하단 대각선
    total = 0
    for i in range(100):
        total += matrix[i][99-i]
        if max_sum < total:
            max_sum = total   
    
    print(f'#{tc} {max_sum}')





# import sys
# sys.stdin = open('input.txt')

# T = 10

# for tc in range(1, T+1):
#     tc = int(input())

#     matrix = []

#     # i, j, a 반복문들 돌리는 변수를 지정
#     # _ => 변수를 활용하지 않은 예정
#     for _ in range(100):
#         numbers = list(map(int, input().split()))
#         matrix.append(numbers)

#     max_total = 0

#     # 가로줄
#     for row in range(len(matrix)):
#         total = 0
#         for col in range(len(matrix[0])):
#             total += matrix[row][col]

#         if max_total < total:
#             max_total = total

#     # 세로줄
#     for col in range(100):
#         total = 0
#         for row in range(100):
#             total += matrix[row][col]

#         if max_total < total:
#             max_total = total


#     # 좌상단 => 우하단 대각선
#     total = 0
#     for i in range(100):
#         total += matrix[i][i]

#     if max_total < total:
#         max_total = total

#     # 우상단 => 좌하단 대각선
#     total = 0
#     for i in range(100):
#         total += matrix[i][99-i]

#     if max_total < total:
#         max_total = total

#     print(max_total)